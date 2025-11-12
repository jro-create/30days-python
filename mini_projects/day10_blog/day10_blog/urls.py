from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth (HTML + session)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # API docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # DRF APIs
    path('api/', include('blog.api_urls')),       # Day 18 read-only
    path('api/v1/', include('blog.api_v1_urls')), # Day 19 write-capable

    # Token auth
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),

    # HTML site
    path('', include('blog.urls')),
]

