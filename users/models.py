from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default_avatar.jpg',
                               upload_to='profile_images',
                               verbose_name='Фотография')
    bio = models.TextField(blank=True, verbose_name='Статус')

    def _str_(self):
        return self.user.username
