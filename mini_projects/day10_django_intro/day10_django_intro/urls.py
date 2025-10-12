from django.contrib import admin
from django.urls import path
from d10_blog import views as d10_blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', d10_blog_views.post_list, name='post_list'),
]

