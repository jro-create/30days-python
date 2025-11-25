from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from blog.models import Post, Comment


class ApiCommentsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alice", password="pass12345")
        self.other = User.objects.create_user(username="bob", password="pass12345")
        self.post = Post.objects.create(title="First", content="Hello", author="alice")
        self.client = APIClient()

    def test_anon_cannot_create_comment(self):
        url = f"/api/v1/posts/{self.post.slug}/comments/"
        r = self.client.post(url, {"content": "hi"}, format="json")
        self.assertEqual(r.status_code, 401)

    def test_auth_can_create_comment(self):
        self.client.login(username="alice", password="pass12345")
        url = f"/api/v1/posts/{self.post.slug}/comments/"
        r = self.client.post(url, {"content": "api ok"}, format="json")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.data["author"], "alice")
        self.assertTrue(Comment.objects.filter(post=self.post, author="alice").exists())

    def test_posts_list_includes_comments_key(self):
        self.client.login(username="alice", password="pass12345")
        Comment.objects.create(post=self.post, author="alice", content="x")
        r = self.client.get("/api/v1/posts/")
        self.assertEqual(r.status_code, 200)
        self.assertTrue("results" in r.data or isinstance(r.data, list))  # pagination off or on
        # Normalize for both cases
        items = r.data if isinstance(r.data, list) else r.data.get("results", [])
        self.assertTrue(isinstance(items, list))
        # at least first item has comments key
        self.assertIn("comments", items[0])

