from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentDeleteView,
    LegacyPostDetailRedirect, LegacyPostEditRedirect, LegacyPostDeleteRedirect,
)

urlpatterns = [
    # List / create
    path("", PostListView.as_view(), name="post_list"),
    path("posts/new/", PostCreateView.as_view(), name="post_create"),

    # Canonical slug-based routes
    path("posts/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<slug:slug>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("posts/<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("posts/<slug:slug>/comment/", CommentCreateView.as_view(), name="comment_create"),

    # ✅ Missing before — add delete-by-id for a specific comment
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),

    # Legacy pk redirects to canonical slug
    path("posts/<int:pk>/",       LegacyPostDetailRedirect.as_view()),
    path("posts/<int:pk>/edit/",  LegacyPostEditRedirect.as_view()),
    path("posts/<int:pk>/delete/",LegacyPostDeleteRedirect.as_view()),
]

