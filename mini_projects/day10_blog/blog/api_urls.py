from django.urls import path
from .api_views import (
    PostListAPI, PostDetailAPI, PostCommentsListAPI, CommentDetailAPI
)

urlpatterns = [
    # /api/posts/ (paginated list)
    path("posts/", PostListAPI.as_view(), name="api_post_list"),

    # /api/posts/<slug>/ (detail with nested comments)
    path("posts/<slug:slug>/", PostDetailAPI.as_view(), name="api_post_detail"),

    # /api/posts/<slug>/comments/ (comments for a post)
    path("posts/<slug:slug>/comments/", PostCommentsListAPI.as_view(), name="api_post_comments"),

    # /api/comments/<id>/ (single comment)
    path("comments/<int:pk>/", CommentDetailAPI.as_view(), name="api_comment_detail"),
]

