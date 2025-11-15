from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView,
    PostDeleteView, CommentCreateView, CommentDeleteView, LegacyPostDetailRedirect,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("posts/new/", PostCreateView.as_view(), name="post_create"),
    path("posts/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<slug:slug>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("posts/<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("posts/<slug:slug>/comment/", CommentCreateView.as_view(), name="comment_create"),
    path("posts/<slug:slug>/comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
    # legacy pk -> slug redirect
    path("posts/<int:pk>/", LegacyPostDetailRedirect.as_view(), name="post_detail_legacy"),
]

