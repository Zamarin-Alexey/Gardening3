from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.urls import reverse


def plant_directory_path(instance, filename):
    return f'images/flowers/plant#{instance.plant.id}/{filename}'


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Plant(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название растения')
    description = models.TextField(verbose_name='Описание растения')
    conditions = models.TextField(verbose_name='Условия ухода')
    planting = models.CharField(max_length=255, verbose_name='Период посадки')
    stages = models.TextField(verbose_name='Стадии роста')
    reproduction = models.TextField(verbose_name='Размножение и рассадка')
    tags = models.CharField(max_length=255, blank=True)
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)], default=0, blank=True)
    category = models.ForeignKey(Category, related_name='Категория', null=True, on_delete=models.SET_NULL)
    # family = models.ForeignKey(Family, related_name='Семейство', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('plant_page', kwargs={'plant_id': self.pk})

    class Meta:
        verbose_name = 'Растениe'
        verbose_name_plural = 'Растения'
        ordering = ['rating']


class ImagePlant(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=plant_directory_path, verbose_name='Фотографии')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Review(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField
    estimation = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    published_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    readers = models.ManyToManyField(User, related_name='reviews', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('review', kwargs={'review_id': self.pk})

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['title']
        unique_together = ('user', 'plant')


