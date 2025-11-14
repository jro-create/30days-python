from django.db import models
from django.utils import timezone
from django.utils.text import slugify

def unique_slugify(instance, value, slug_field_name="slug"):
    """
    Make a unique slug from 'value' by suffixing -1, -2, ... if needed.
    """
    slug_base = slugify(value) or "post"
    slug = slug_base
    ModelClass = instance.__class__
    i = 1
    while ModelClass.objects.filter(**{slug_field_name: slug}).exclude(pk=instance.pk).exists():
        i += 1
        slug = f"{slug_base}-{i}"
    return slug

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100)  # username as simple string (kept per earlier days)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    # ✅ new optional image
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)

    class Meta:
        ordering = ["-date_posted"]

    def save(self, *args, **kwargs):
        # generate slug if missing or title changed slug basis
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

