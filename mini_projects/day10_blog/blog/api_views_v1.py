from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Post, Comment
from .api_permissions import IsOwnerOrReadOnly
from .api_serializers import (
    PostListSerializer, PostDetailSerializer, PostWriteSerializer,
    CommentSerializer, CommentWriteSerializer
)

class PostViewSet(ModelViewSet):
    """
    CRUD for posts.
    - lookup by slug
    - author set from request.user.username on create
    - only owner can update/delete
    - /api/v1/posts/<slug>/comments/ supports:
        GET  -> list comments
        POST -> create a comment (any authenticated user)
    """
    queryset = Post.objects.all().order_by("-date_posted")
    lookup_field = "slug"
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

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
        post = self.get_object()  # DRF will check IsAuthenticatedOrReadOnly; no owner check here

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
    - list/retrieve open
    - create allowed (requires 'post_slug' in payload) or use the post action above
    - update/delete owner-only
    """
    queryset = Comment.objects.all().order_by("-created_at")
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

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

