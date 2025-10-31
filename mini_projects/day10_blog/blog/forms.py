from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "author", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Post title"}),
            "author": forms.TextInput(attrs={"placeholder": "Your name"}),
            "content": forms.Textarea(attrs={"rows": 6, "placeholder": "Write your post..."})
        }

