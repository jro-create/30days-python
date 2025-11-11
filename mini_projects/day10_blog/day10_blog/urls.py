from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth for HTML and SessionAuth
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # API (read-only from Day 18)
    path('api/', include('blog.api_urls')),

    # API v1 (write-capable for Day 19)
    path('api/v1/', include('blog.api_v1_urls')),

    # Token endpoint (POST username/password to get a token)
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),

    # HTML site
    path('', include('blog.urls')),
]

