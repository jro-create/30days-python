from django.db.models import Count
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication,
    BasicAuthentication,
)
from rest_framework.pagination import PageNumberPagination

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class SmallResultsPagination(PageNumberPagination):
    """
    Simple pagination so list endpoints return a dict with
    {count, next, previous, results}, which is what your tests expect.
    We keep page_size high so for small datasets you effectively see all posts.
    """
    page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    """
    Posts API:
      - lookup by slug
      - anyone can read; writes are protected by IsOwnerOrReadOnly
      - author is set from request.user.username on create/update
      - list endpoint is paginated (so r.data has 'results')
      - each Post is annotated with comment_count
    """
    queryset = (
        Post.objects.all()
        .annotate(comment_count=Count("comments"))
        .order_by("-created_at")
    )
    serializer_class = PostSerializer
    lookup_field = "slug"

    authentication_classes = [
        SessionAuthentication,
        TokenAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = SmallResultsPagination  # ✅ keep pagination ON

    def perform_create(self, serializer):
        # called on POST /api/v1/posts/
        serializer.save(author=self.request.user.username)

    def perform_update(self, serializer):
        # called on PUT/PATCH /api/v1/posts/<slug>/
        serializer.save(author=self.request.user.username)

    @action(
        detail=True,
        methods=["get", "post"],
        url_path="comments",
        # ⚠️ IMPORTANT:
        # We do NOT override authentication_classes here so SessionAuth keeps working.
        permission_classes=[permissions.AllowAny],  # we handle 401 manually for anon POST
    )
    def comments(self, request, slug=None):
        """
        GET  /api/v1/posts/<slug>/comments/  -> 200 list (anyone)
        POST /api/v1/posts/<slug>/comments/  -> 201 when authenticated, else 401
        """
        post = self.get_object()

        # --- GET: list comments (always allowed) ---
        if request.method.lower() == "get":
            qs = post.comments.order_by("-created_at")
            data = CommentSerializer(
                qs,
                many=True,
                context={"request": request},
            ).data
            return Response(data, status=status.HTTP_200_OK)

        # --- POST: require authentication ---
        user = getattr(request, "user", None)
        if not user or not user.is_authenticated:
            # This matches test_anon_cannot_create_comment (expects 401)
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        content = (request.data.get("content") or "").strip()
        if not content:
            return Response(
                {"detail": "content is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        comment = Comment.objects.create(
            post=post,
            author=user.username,
            content=content,
        )
        data = CommentSerializer(
            comment,
            context={"request": request},
        ).data
        return Response(data, status=status.HTTP_201_CREATED)

