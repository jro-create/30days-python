from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def home(request):
    # If your URL name 'home' is already used elsewhere, rename this to post_list and update urls.
    posts = Post.objects.all().order_by("-date_posted")
    return render(request, "blog/post_list.html", {"posts": posts})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")   # after create, go back to list
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form, "action": "Create"})


