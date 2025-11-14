from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from django.shortcuts import get_object_or_404

# ✅ new imports for filtering/search/ordering
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Post, Comment
from .api_permissions import IsOwnerOrReadOnly
from .api_serializers import (
    PostListSerializer, PostDetailSerializer, PostWriteSerializer,
    CommentSerializer, CommentWriteSerializer
)

class PostViewSet(ModelViewSet):
    """
    CRUD for posts (lookup by slug).
    - Filters:  ?author=<name>
    - Search:   ?search=term   (title, content, author)
    - Ordering: ?ordering=title | -date_posted | author
    - Comments sub-action: /api/v1/posts/<slug>/comments/  (GET, POST)
    """
    queryset = Post.objects.all().order_by("-date_posted")
    lookup_field = "slug"
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # ✅ enable server-side filter/search/ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["author"]              # exact match filter
    search_fields = ["title", "content", "author"]  # text search
    ordering_fields = ["date_posted", "title", "author"]
    ordering = ["-date_posted"]                # default

    def get_serializer_class(self):
        # Use comment serializers for the custom 'comments' action
        if getattr(self, "action", None) == "comments":
            if self.request.method == "GET":
                return CommentSerializer
            return CommentWriteSerializer

        if self.action == "list":
            return PostListSerializer
        if self.action == "retrieve":
            return PostDetailSerializer
        # create/update/partial_update
        return PostWriteSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.username)

    def perform_update(self, serializer):
        # prevent author changes
        serializer.save(author=self.get_object().author)

    @action(
        detail=True,
        methods=["get", "post"],
        url_path="comments",
        permission_classes=[IsAuthenticatedOrReadOnly],  # allow any logged-in user to comment
    )
    def comments(self, request, slug=None):
        """
        GET  /api/v1/posts/<slug>/comments/   -> list comments
        POST /api/v1/posts/<slug>/comments/   -> create a comment (body: {"content": "..."} )
        """
        post = self.get_object()

        if request.method == "GET":
            qs = post.comments.all().order_by("-created_at")
            data = CommentSerializer(qs, many=True).data
            return Response(data, status=status.HTTP_200_OK)

        # POST
        ser_in = CommentWriteSerializer(data=request.data)
        ser_in.is_valid(raise_exception=True)
        comment = Comment.objects.create(
            post=post,
            author=request.user.username,
            content=ser_in.validated_data["content"],
        )
        return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)


class CommentViewSet(ModelViewSet):
    """
    CRUD for comments by id.
    - Filters:  ?author=<name>, ?post__slug=<slug>
    - Search:   ?search=term  (content, author)
    - Ordering: ?ordering=-created_at | author
    """
    queryset = Comment.objects.all().order_by("-created_at")
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # ✅ enable filter/search/ordering on comments, too
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["author", "post__slug"]
    search_fields = ["content", "author"]
    ordering_fields = ["created_at", "author"]
    ordering = ["-created_at"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CommentSerializer
        return CommentWriteSerializer

    def perform_create(self, serializer):
        post_slug = self.request.data.get("post_slug")
        if not post_slug:
            from rest_framework.exceptions import ValidationError
            raise ValidationError({"post_slug": "Required (or use POST /posts/<slug>/comments/)."})
        post = get_object_or_404(Post, slug=post_slug)
        serializer.save(post=post, author=self.request.user.username)

    def perform_update(self, serializer):
        obj = self.get_object()
        serializer.save(post=obj.post, author=obj.author)

