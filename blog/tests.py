from django.test import TestCase

from django.contrib.auth.models import User
from .models import Post, Image, Comment
from datetime import datetime


class BlogTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(
            title='Test Post',
            body='This is a test post.',
            user=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertIsInstance(self.post.publish_date, datetime)

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_comment_creation(self):
        comment = Comment.objects.create(
            body='This is a test comment.',
            user=self.user,
            post=self.post
        )
        self.assertEqual(comment.body, 'This is a test comment.')
        self.assertEqual(comment.post, self.post)

    # Additional tests for Image model and other aspects of Post and Comment models
