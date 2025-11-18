from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "updated_at")  # add "reading_time" or "summary" if desired
    search_fields = ("title", "author", "content")
    list_filter = ("author", "created_at")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_at")
    search_fields = ("author", "content")
    list_filter = ("created_at",)

