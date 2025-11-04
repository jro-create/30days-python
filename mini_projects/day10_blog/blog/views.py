from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user.username
        messages.success(self.request, "Post created successfully.")
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user.username

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to edit this post.")
        return super().handle_no_permission()

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully.")
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user.username

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to delete this post.")
        return super().handle_no_permission()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Post deleted.")
        return super().delete(request, *args, **kwargs)

# ---- Comments ----

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"  # fallback

    def dispatch(self, request, *args, **kwargs):
        # Accept post id from URL or hidden input; guard invalid values
        raw_id = kwargs.get("pk") or request.POST.get("post_id")
        try:
            post_id = int(raw_id)
        except (TypeError, ValueError):
            messages.error(request, "Invalid post id.")
            return redirect("post_list")

        self.post_obj = get_object_or_404(Post, pk=post_id)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.post = self.post_obj
        form.instance.author = self.request.user.username
        messages.success(self.request, "Comment added.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.post_obj.pk})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def test_func(self):
        c = self.get_object()
        return (c.author == self.request.user.username) or (c.post.author == self.request.user.username)

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to delete this comment.")
        return super().handle_no_permission()

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.post.pk})

