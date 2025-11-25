from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.test import Client as HtmlClient

User = get_user_model()

class HtmlRoutesTests(TestCase):
    def setUp(self):
        # create a post using the API to generate slug consistently
        self.user = User.objects.create_user(username="owner", password="pass12345")
        api = APIClient()
        api.login(username="owner", password="pass12345")
        r = api.post("/api/v1/posts/", {
            "title": "Visible Post",
            "content": "HTML body",
            "author": self.user.pk
        }, format="json")
        self.slug = r.data["slug"]
        api.logout()
        self.html = HtmlClient()

    def test_homepage_loads(self):
        r = self.html.get("/")
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "My Blog Posts")

    def test_post_detail_page_loads(self):
        r = self.html.get(f"/posts/{self.slug}/")
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "Visible Post")

