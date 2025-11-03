from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 5  # 👈 pagination enabled

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # We won't expose 'author' in the form; set it automatically
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        # Assign author to the logged-in username
        form.instance.author = self.request.user.username
        messages.success(self.request, "Post created successfully.")
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]  # author not editable
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        # Only the original author may edit
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


