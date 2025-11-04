from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentDeleteView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("posts/new/", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),

    # comments
    path("posts/<int:pk>/comment/", CommentCreateView.as_view(), name="comment_create"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),

    # optional aliases (singular); no names to avoid confusion
    path("post/<int:pk>/", PostDetailView.as_view()),
    path("post/<int:pk>/edit/", PostUpdateView.as_view()),
    path("post/<int:pk>/delete/", PostDeleteView.as_view()),
]

