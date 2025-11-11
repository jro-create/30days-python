from rest_framework import serializers
from .models import Post, Comment

# ----- Read serializers (Day 18) -----
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

# ----- Write serializers (Day 19) -----
class PostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content"]  # author set in view from request.user

class CommentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content"]  # post set in view; author set from request.user

