from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, View
)
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import PostForm, CommentForm


# ---------- Post list & detail ----------

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        post = self.object
        # Support either related_name="comments" or default comment_set
        rel = getattr(post, "comments", None)
        ctx["comments"] = rel.all() if rel is not None else post.comment_set.all()
        ctx["comment_form"] = CommentForm()
        return ctx


# ---------- Create / Update / Delete posts ----------

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    form_class = PostForm  # single source of truth; do NOT declare `fields`

    def form_valid(self, form):
        # Your project stores author as a string (username)
        form.instance.author = self.request.user.username
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post_detail", kwargs={"slug": self.object.slug})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    form_class = PostForm
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.get_object().author == self.request.user.username

    def get_success_url(self):
        return reverse("post_detail", kwargs={"slug": self.object.slug})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("post_list")  # class attribute needs reverse_lazy

    def test_func(self):
        return self.get_object().author == self.request.user.username


# ---------- Comments ----------

class CommentCreateView(LoginRequiredMixin, View):
    """Create a comment under a post (POST only)."""
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.username
            comment.save()
        return HttpResponseRedirect(reverse("post_detail", kwargs={"slug": slug}))


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    """Delete a comment (POST only). Route carries both post slug and comment pk."""
    def dispatch(self, request, *args, **kwargs):
        self.post_obj = get_object_or_404(Post, slug=kwargs["slug"])
        self.comment = get_object_or_404(Comment, pk=kwargs["pk"], post=self.post_obj)
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        # Only the comment author (or superuser) can delete
        return (
            self.comment.author == self.request.user.username
            or self.request.user.is_superuser
        )

    def post(self, request, slug, pk):
        self.comment.delete()
        return HttpResponseRedirect(reverse("post_detail", kwargs={"slug": slug}))


# ---------- Legacy redirects (keep old pk-based URLs working) ----------

class LegacyPostDetailRedirect(View):
    """Support old /posts/<pk>/ by redirecting to canonical /posts/<slug>/. """
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return redirect("post_detail", slug=post.slug)

