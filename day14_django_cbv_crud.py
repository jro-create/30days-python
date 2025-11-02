"""
Day 14: Class-Based Views (CBVs) for CRUD
-----------------------------------------

WHY THIS MATTERS
- CBVs reduce boilerplate and give you battle-tested patterns for List, Detail, Create, Update, Delete.

CORE CBVs YOU'LL USE
- ListView: list multiple objects
- DetailView: show a single object
- CreateView: create a new object
- UpdateView: edit an existing object
- DeleteView: delete an object

PATTERNS
- url -> CBV.as_view() -> template_name or default naming
- success_url (reverse_lazy) for redirects after Create/Update/Delete
- LoginRequiredMixin to protect actions (requires Day 13 settings: LOGIN_URL, LOGIN_REDIRECT_URL)

DEFAULT TEMPLATE NAMES (if not overridden)
- <app>/<model>_list.html
- <app>/<model>_detail.html
- <app>/<model>_form.html
- <app>/<model>_confirm_delete.html

EXAMPLE (for Post model)
-------------------------------------------------
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'author', 'content']
    success_url = reverse_lazy('post_list')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'author', 'content']
    success_url = reverse_lazy('post_list')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

NOTES
- If you keep author as a CharField, anyone can “claim” authorship; real apps use a FK to User.
- CBVs look for templates at blog/post_list.html, blog/post_detail.html, etc., unless you set template_name.

TODAY’S GOAL
- Replace function views with CBVs for the blog.
- Add List, Detail, Create, Edit, Delete + links between them.
"""
print("✅ Day 14 lesson ready: read it, then implement the mini-project steps.")

