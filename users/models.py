from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'profile_images/user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default_avatar.png',
                               upload_to=user_directory_path,
                               verbose_name='Фотография')
    bio = models.TextField(blank=True, verbose_name='Статус')

    def _str_(self):
        return self.user.username
