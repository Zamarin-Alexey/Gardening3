from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст поста')
    tags = models.CharField(blank=True, max_length=255, verbose_name='Теги')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-publish_date']


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class Comment(models.Model):
    body = models.TextField
    image = models.ImageField(upload_to='images/')
    publish_date = models.DateTimeField(auto_now_add=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)


class Plant(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField
    image = models.ImageField(upload_to='images/')
    conditions = models.TextField
    planting_period = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)


class Review(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField
    estimation = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    image = models.ImageField(upload_to='images/')
    tags = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)


class UserPlant(models.Model):
    title = models.CharField(max_length=255)
    date_start = models.DateField(auto_now=True)
    date_finish = models.DateField
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)
