from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .api_serializers import (
    PostListSerializer, PostDetailSerializer, CommentSerializer
)

class PostListAPI(ListAPIView):
    queryset = Post.objects.all().order_by("-date_posted")
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]

class PostDetailAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    lookup_field = "slug"
    serializer_class = PostDetailSerializer
    permission_classes = [AllowAny]

class PostCommentsListAPI(ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        post = get_object_or_404(Post, slug=self.kwargs.get("slug"))
        return post.comments.all().order_by("-created_at")

class CommentDetailAPI(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

