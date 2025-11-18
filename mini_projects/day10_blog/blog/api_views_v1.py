from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from .models import Post, Comment
from .api_permissions import IsOwnerOrReadOnly
from .api_serializers import (
    PostListSerializer, PostDetailSerializer, PostWriteSerializer,
    CommentSerializer, CommentWriteSerializer
)

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by("-date_posted")
    lookup_field = "slug"
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["author"]
    search_fields = ["title", "content", "author"]
    ordering_fields = ["date_posted", "title", "author"]
    ordering = ["-date_posted"]

    parser_classes = [JSONParser, FormParser, MultiPartParser]  # 🔑 allow file uploads

    def get_serializer_class(self):
        if getattr(self, "action", None) == "comments":
            return CommentSerializer if self.request.method == "GET" else CommentWriteSerializer
        if self.action == "list":
            return PostListSerializer
        if self.action == "retrieve":
            return PostDetailSerializer
        return PostWriteSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.username)

    def perform_update(self, serializer):
        serializer.save(author=self.get_object().author)

    @action(detail=True, methods=["get", "post"], url_path="comments",
            permission_classes=[IsAuthenticatedOrReadOnly])
    def comments(self, request, slug=None):
        post = self.get_object()
        if request.method == "GET":
            qs = post.comments.all().order_by("-created_at")
            return Response(CommentSerializer(qs, many=True).data, status=status.HTTP_200_OK)
        ser_in = CommentWriteSerializer(data=request.data)
        ser_in.is_valid(raise_exception=True)
        comment = Comment.objects.create(
            post=post, author=request.user.username, content=ser_in.validated_data["content"]
        )
        return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["author", "post__slug"]
    search_fields = ["content", "author"]
    ordering_fields = ["created_at", "author"]
    ordering = ["-created_at"]

    def get_serializer_class(self):
        return CommentSerializer if self.action in ["list", "retrieve"] else CommentWriteSerializer

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

