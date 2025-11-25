from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

class PostWriteAPITests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username="owner", password="pass12345")
        self.other = User.objects.create_user(username="other", password="pass12345")
        self.api = APIClient()

        # Owner creates a post (auth via session login for simplicity)
        self.api.login(username="owner", password="pass12345")
        r = self.api.post(
            "/api/v1/posts/",  {
                "title": "Owner Post",
                "content": "content",
                "author": self.owner.pk
         },format="json")
        self.assertEqual(r.status_code, 201)
        self.slug = r.data["slug"]
        # and a comment
        rc = self.api.post(f"/api/v1/posts/{self.slug}/comments/", {"content": "owner comment"}, format="json")
        self.assertEqual(rc.status_code, 201)
        self.api.logout()

    def test_create_post_requires_auth(self):
        api = APIClient()
        r = api.post("/api/v1/posts/", {"title": "No Auth", "content": "x"}, format="json")
        self.assertIn(r.status_code, (401, 403))  # unauthenticated should not create

    def test_owner_can_update_own_post(self):
        api = APIClient()
        api.login(username="owner", password="pass12345")
        r = api.patch(f"/api/v1/posts/{self.slug}/", {"content": "edited"}, format="json")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data["content"], "edited")
        api.logout()

    def test_other_user_cannot_update_someone_elses_post(self):
        api = APIClient()
        api.login(username="other", password="pass12345")
        r = api.patch(f"/api/v1/posts/{self.slug}/", {"content": "hack"}, format="json")
        self.assertEqual(r.status_code, 403)  # blocked by IsOwnerOrReadOnly
        api.logout()

    def test_comment_requires_auth(self):
        api = APIClient()
        r = api.post(f"/api/v1/posts/{self.slug}/comments/", {"content": "anon"}, format="json")
        self.assertIn(r.status_code, (401, 403))  # must be logged in

    def test_authenticated_user_can_comment_any_post(self):
        api = APIClient()
        api.login(username="other", password="pass12345")
        r = api.post(f"/api/v1/posts/{self.slug}/comments/", {"content": "hello!"}, format="json")
        self.assertEqual(r.status_code, 201)
        api.logout()

