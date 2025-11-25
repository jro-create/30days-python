from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment


class HtmlCommentsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alice", password="pass12345")
        self.other = User.objects.create_user(username="bob", password="pass12345")
        self.post = Post.objects.create(
            title="First", content="Hello", author="alice"
        )

    def test_anon_sees_comments_but_cannot_post(self):
        url = reverse("post_detail", kwargs={"slug": self.post.slug})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        create_url = reverse("comment_create", kwargs={"slug": self.post.slug})
        res2 = self.client.post(create_url, {"content": "Hi"})
        # should redirect to login
        self.assertEqual(res2.status_code, 302)
        self.assertIn(reverse("login"), res2.url)

    def test_authenticated_user_can_create_comment(self):
        self.client.login(username="alice", password="pass12345")
        create_url = reverse("comment_create", kwargs={"slug": self.post.slug})
        res = self.client.post(create_url, {"content": "Nice post"})
        self.assertEqual(res.status_code, 302)
        self.assertTrue(Comment.objects.filter(post=self.post, author="alice").exists())

    def test_only_owner_or_superuser_can_delete_comment(self):
        self.client.login(username="alice", password="pass12345")
        cmt = Comment.objects.create(post=self.post, author="alice", content="mine")

        # other user tries to delete -> 403
        self.client.logout()
        self.client.login(username="bob", password="pass12345")
        del_url = reverse("comment_delete", kwargs={"slug": self.post.slug, "pk": cmt.pk})
        res = self.client.post(del_url)
        self.assertEqual(res.status_code, 403)

        # owner can delete
        self.client.logout()
        self.client.login(username="alice", password="pass12345")
        res2 = self.client.post(del_url)
        self.assertEqual(res2.status_code, 302)
        self.assertFalse(Comment.objects.filter(pk=cmt.pk).exists())

