from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField
    image = models.ImageField(upload_to='image/')
    tags = models.CharField(max_length=255)
    publish_date = models.DateTimeField(auto_now_add=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


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

class User_Plant(models.Model):
    title = models.CharField(max_length=255)
    date_start = models.DateField(auto_now=True)
    date_finish = models.DateField
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)
