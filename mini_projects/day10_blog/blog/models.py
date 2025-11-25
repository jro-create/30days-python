from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, db_index=True)
    content = models.TextField()
    # NEW optional field
    summary = models.TextField(blank=True, null=True, help_text="Short teaser/SEO snippet")
    # We store the author's username (string) to avoid FK complexity while learning
    author = models.CharField(max_length=150, db_index=True)
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.title} ({self.slug})"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # Autogenerate slug once if missing; keep stable for existing content
        if not self.slug:
            base = slugify(self.title) or "post"
            slug = base
            n = 2
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=150, db_index=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        ts = timezone.localtime(self.created_at).strftime("%Y-%m-%d %H:%M")
        return f"Comment by {self.author} on {self.post.slug} at {ts}"

