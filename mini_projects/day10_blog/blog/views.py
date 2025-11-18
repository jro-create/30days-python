from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import logout
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        post = self.get_object()
        ctx["comments"] = post.comments.order_by("-created_at")
        if self.request.user.is_authenticated:
            ctx["comment_form"] = CommentForm()
        return ctx


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    form_class = PostForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user.username
        obj.save()
        messages.success(self.request, "Post created.")
        return redirect(obj.get_absolute_url())


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    form_class = PostForm
    slug_field = "slug"
    slug_url_kwarg = "slug"
    raise_exception = True  # return 403 instead of redirect

    def test_func(self):
        return self.get_object().author == self.request.user.username

    def form_valid(self, form):
        obj = form.save(commit=False)
        # keep original author
        obj.author = self.get_object().author
        obj.save()
        messages.success(self.request, "Post updated.")
        return redirect(obj.get_absolute_url())


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("post_list")
    raise_exception = True

    def test_func(self):
        return self.get_object().author == self.request.user.username


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.username
            comment.save()
            messages.success(request, "Comment added.")
        else:
            messages.error(request, "Could not add comment. Please check the form.")
        return redirect(post.get_absolute_url())

    def get(self, request, slug):
        return HttpResponseNotAllowed(["POST"])


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"
    pk_url_kwarg = "pk"
    raise_exception = True

    def get_queryset(self):
        return Comment.objects.select_related("post")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user.username or self.request.user.is_superuser

    def get_success_url(self):
        return self.get_object().post.get_absolute_url()


class LegacyPostDetailRedirect(View):
    """
    Keep legacy pk route and redirect to canonical slug route.
    """
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return redirect(post.get_absolute_url(), permanent=True)


class LogoutPostOnlyView(LoginRequiredMixin, View):
    """
    Enforce POST-only logout to match your guardrail.
    """
    def post(self, request):
        logout(request)
        messages.info(request, "Logged out.")
        return redirect("post_list")

    def get(self, request):
        return HttpResponseNotAllowed(["POST"])

