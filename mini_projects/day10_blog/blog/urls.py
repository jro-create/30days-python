from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/new/", views.post_create, name="post_create"),
]

