from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, ExtendUser
from plants.models import Plant
from blog.models import Post, Comment

class UsersModelsTestCase(TestCase):

    def setUp(self):
        # Создаем необходимые объекты для тестирования
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.plant = Plant.objects.create(title='Test Plant', description='Test description')

    def test_profile_model(self):
        # Тестирование модели Profile
        profile = Profile.objects.create(user=self.user, bio='Test bio')
        self.assertEqual(profile.__str__(), 'testuser')  # Проверяем метод __str__

    def test_extenduser_model(self):
        # Тестирование модели ExtendUser
        extend_user = ExtendUser.objects.create(user=self.user)
        extend_user.plants.add(self.plant)
        self.assertEqual(extend_user.user.username, 'testuser')  # Проверяем связь с пользователем
        self.assertEqual(extend_user.plants.count(), 1)  # Проверяем связь с растениями

    def test_models_relations(self):
        # Тестирование связей между моделями
        profile = Profile.objects.create(user=self.user, bio='Test bio')
        extend_user = ExtendUser.objects.create(user=self.user)
        extend_user.plants.add(self.plant)
        post = Post.objects.create(title='Test Post', body='Test body', user=self.user)
        comment = Comment.objects.create(body='Test Comment', user=self.user, post=post)

        # Проверяем связи между моделями
        self.assertEqual(profile.user, self.user)
        self.assertEqual(extend_user.user, self.user)
        self.assertEqual(post.user, self.user)
        self.assertEqual(comment.user, self.user)
        self.assertEqual(post.user, comment.user)
        self.assertEqual(extend_user.plants.first(), self.plant)
        self.assertEqual(post.user.profile, profile)
