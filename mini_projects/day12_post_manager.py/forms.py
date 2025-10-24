from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "author", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Title"}),
            "author": forms.TextInput(attrs={"placeholder": "Author name"}),
            "content": forms.Textarea(attrs={"rows": 6}),
        }

    # Example of per-field validation
    def clean_title(self):
        title = self.cleaned_data.get("title", "")
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters.")
        return title

