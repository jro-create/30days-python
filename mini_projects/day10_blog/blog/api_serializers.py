from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "content", "created_at"]

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "slug", "author", "date_posted"]

class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["title", "slug", "author", "date_posted", "content", "comments"]

