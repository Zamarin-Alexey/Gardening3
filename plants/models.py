from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.urls import reverse
import datetime


def plant_directory_path(instance, filename):
    return f'images/flowers/plant#{instance.plant.id}/{filename}'


class Plant(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    conditions = models.TextField(verbose_name='Условия')
    period_start = models.DateField(default=datetime.date.today(), verbose_name='Начало посадки',)
    period_finish = models.DateField(default=datetime.date.today(), verbose_name='Конец посадки',)
    tags = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('plant_page', kwargs={'plant_id': self.pk})

    class Meta:
        verbose_name = 'Растениe'
        verbose_name_plural = 'Растения'
        ordering = ['title']


class PhotoPlant(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=plant_directory_path, verbose_name='Фотографии')
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

class Review(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField
    estimation = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    image = models.ImageField(upload_to='images/')
    tags = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)


class UserPlant(models.Model):
    title = models.CharField(max_length=255)
    date_start = models.DateField(auto_now=True)
    date_finish = models.DateField
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)
