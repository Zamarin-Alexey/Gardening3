from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст поста')
    tags = models.CharField(blank=True, max_length=255, verbose_name='Теги')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    likes = models.IntegerField(blank=True, default=0)
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
    body = models.TextField(blank=True, verbose_name='Текст комментария')
    image = models.ImageField(blank=True, upload_to='images/', verbose_name='Изображение')
    publish_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['publish_date']