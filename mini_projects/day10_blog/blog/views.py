from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']  # newest first
    template_name = "blog/post_list.html"   # keeps your existing template
    context_object_name = "posts"           # use 'posts' in template

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "author", "content"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "author", "content"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")




