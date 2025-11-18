from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from blog.api_views import PostViewSet
from rest_framework.routers import DefaultRouter

# DRF router
router = DefaultRouter()
router.register("posts", PostViewSet, basename="post")

# drf-spectacular schema
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

from blog.views import LogoutPostOnlyView

urlpatterns = [
    path("admin/", admin.site.urls),

    # HTML app
    path("", include("blog.urls")),

    # Auth (logout is POST-only via custom view)
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", LogoutPostOnlyView.as_view(), name="logout"),

    # API
    path("api/v1/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

# Serve media in debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

