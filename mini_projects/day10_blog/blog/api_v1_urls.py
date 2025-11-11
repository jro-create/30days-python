from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views_v1 import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='v1_posts')
router.register(r'comments', CommentViewSet, basename='v1_comments')

urlpatterns = [
    path('', include(router.urls)),
]

