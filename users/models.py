from django.db import models
from django.contrib.auth.models import User

from plants.models import Plant, Review
from blog.models import Post


def user_directory_path(instance, filename):
    return 'profile_images/user_{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    avatar = models.ImageField(default='default_avatar.png',
                               upload_to=user_directory_path,
                               verbose_name='Фотография')
    bio = models.TextField(blank=True, verbose_name='Статус')
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Используйте OneToOneField
    plants = models.ManyToManyField(Plant)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Учётные записи'


class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)  # Добавьте unique=True
    plants = models.ManyToManyField(Plant)
    liked_posts = models.ManyToManyField(Post)
    liked_reviews = models.ManyToManyField(Review)

    def __str__(self):  # Замените _str_ на __str__
        return self.user.username


# class UserFollowing(models.Model):
#     user_id = models.ForeignKey("User", related_name="following", on_delete=models.CASCADE)
#     following_user_id = models.ForeignKey("User", related_name="followers", on_delete=models.CASCADE)