from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import string, random

def _rand_suffix(n=4):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)  # simple for now
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:120] or "post"
            candidate = base
            i = 0
            while Post.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                i += 1
                candidate = f"{base}-{_rand_suffix()}"
                if i > 50:
                    candidate = f"{base}-{_rand_suffix(6)}"
                    break
            self.slug = candidate
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"

