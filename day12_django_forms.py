"""
Day 12: Django Forms and ModelForms
-----------------------------------

📘 Overview:
Django Forms simplify collecting and validating user input. 
They help convert HTTP POST data into Python objects and ensure security (e.g., CSRF protection).

GOAL
- Learn how to collect and validate user input with Django Forms.
- Support Create, Update, Delete (CRUD) via forms.
- Understand form validation and security basics (CSRF, cleaned_data).

KEY CONCEPTS
- forms.Form vs forms.ModelForm
  - forms.Form: manual fields; good for custom logic.
  - forms.ModelForm: maps directly to a model; quickest for CRUD.
- request.method == "POST" → handle submitted form
- form.is_valid() → use form.cleaned_data
- Use {% csrf_token %} in templates to avoid CSRF errors
- Redirect after POST (Post/Redirect/Get pattern) to avoid duplicate submits

COMMON WORKFLOW (CREATE)
1. Create a ModelForm for the model.
2. Provide a view that:
   - shows form on GET
   - validates & saves on POST
3. Add URL route to access the view
4. Create a template with the form and {% csrf_token %}

SAMPLE ModelForm (for a blog Post model)
----------------------------------------
# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "author", "content"]

Handling in a view
------------------
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})

Form template essentials
------------------------
<!-- blog/templates/blog/post_form.html -->
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Save</button>
</form>

VALIDATION & TIPS
- Use clean_<fieldname>() methods in forms to validate single fields.
- Use clean() to validate cross-field constraints.
- Always validate on server even if you add client-side checks.
- Use messages framework for UX (success/error notices).

✅ Exercise:
Review this code, understand the flow (form creation → validation → saving).
You’ll now apply this knowledge in your mini project: a simple Post Manager app.
"""

print("✅ Day 12 lesson file created. Day 12 Django Forms lesson ready — proceed to mini project.")
