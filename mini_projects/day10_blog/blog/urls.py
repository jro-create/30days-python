from django.urls import path
# Import the function-based views file for legacy/simple views
from . import views 
# Import all class-based views using parentheses for clean multi-line imports
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    CommentCreateView, 
    CommentDeleteView, 
    LegacyPostDetailRedirect,
)

urlpatterns = [
    # 1. Main List View (Home page)
    path("", PostListView.as_view(), name="post_list"),

    # 2. CRUD/Action Views (MUST be before post_detail to be specific)
    path("posts/new/", PostCreateView.as_view(), name="post_create"),
    path("posts/<slug:slug>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("posts/<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),

    # 3. Comment Actions
    path("posts/<slug:slug>/comment/", CommentCreateView.as_view(), name="comment_create"),
    path("posts/<slug:slug>/comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),

    # 4. Legacy PK Redirect (Stricter 'int:pk' must come BEFORE the general 'slug:slug')
    path("posts/<int:pk>/", LegacyPostDetailRedirect.as_view(), name="post_detail_legacy"),

    # 5. Main Detail View (General slug view)
    path("posts/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),

    # 6. Remove the conflicting function-based view, as the class-based one is now the main detail view.
    # If you still need the function-based view, rename its 'name' attribute:
    # path('post/<int:pk>/view-by-pk/', views.post_detail_view, name='post_detail_by_pk'),
]
