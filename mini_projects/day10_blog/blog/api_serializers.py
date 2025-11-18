from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "content", "created_at"]

class PostListSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(read_only=True)
    class Meta:
        model = Post
        fields = ["title", "slug", "author", "date_posted", "cover"]

class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    cover = serializers.ImageField(read_only=True)
    class Meta:
        model = Post
        fields = ["title", "slug", "author", "date_posted", "content", "cover", "comments"]

class PostWriteSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    author = serializers.CharField(read_only=True)
    date_posted = serializers.DateTimeField(read_only=True)
    cover = serializers.ImageField(required=False, allow_null=True)
    class Meta:
        model = Post
        fields = ["title", "content", "cover", "slug", "author", "date_posted"]

class CommentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content"]

