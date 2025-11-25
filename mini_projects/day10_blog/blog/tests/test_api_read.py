from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

class ApiReadTests(TestCase):
    def setUp(self):
        # Create a user and token-style client
        self.user = User.objects.create_user(username="owner", password="pass12345")
        self.api = APIClient()
        # Authenticate and create a post via API so slug is generated the real way
        self.api.login(username="owner", password="pass12345")
        resp = self.api.post(
            "/api/v1/posts/",
            {
                "title": "Post One",
                "content": "Body",
                "author": self.user.pk
            },
            format="json"
        )
        self.assertEqual(resp.status_code, 201)
        self.slug = resp.data["slug"]
        # Add one comment via the action endpoint
        resp2 = self.api.post(f"/api/v1/posts/{self.slug}/comments/", {"content": "Nice post!"}, format="json")
        self.assertEqual(resp2.status_code, 201)
        self.api.logout()

    def test_posts_list_ok(self):
        api = APIClient()
        r = api.get("/api/v1/posts/")
        self.assertEqual(r.status_code, 200)
        self.assertIn("results", r.data)  # pagination keys exist

    def test_post_detail_includes_comments(self):
        api = APIClient()
        r = api.get(f"/api/v1/posts/{self.slug}/")  # Day 18 read-only detail
        self.assertEqual(r.status_code, 200)
        self.assertIn("comments", r.data)
        self.assertTrue(len(r.data["comments"]) >= 1)

    def test_post_comments_list_ok(self):
        api = APIClient()
        r = api.get(f"/api/v1/posts/{self.slug}/comments/")
        self.assertEqual(r.status_code, 200)
        self.assertIsInstance(r.data, list)
        self.assertGreaterEqual(len(r.data), 1)

