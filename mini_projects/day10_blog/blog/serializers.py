from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "content", "created_at", "updated_at"]


class PostSerializer(serializers.ModelSerializer):
    # Make slug and author read-only; cover optional
    slug = serializers.SlugField(read_only=True)
    author = serializers.CharField(read_only=True)
    cover = serializers.ImageField(required=False, allow_null=True)

    # Expose comments inline (read-only) and an annotated count
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "content",
            "author",
            "cover",
            "created_at",
            "updated_at",
            "comment_count",
            "comments",
        ]

