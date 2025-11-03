from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    # list + create (canonical)
    path("", PostListView.as_view(), name="post_list"),
    path("posts/new/", PostCreateView.as_view(), name="post_create"),

    # canonical detail/edit/delete (plural)
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),

    # backward-compatible aliases (singular) – prevents NoReverseMatch if you type /post/1/
    path("post/<int:pk>/", PostDetailView.as_view()),
    path("post/<int:pk>/edit/", PostUpdateView.as_view()),
    path("post/<int:pk>/delete/", PostDeleteView.as_view()),
]

