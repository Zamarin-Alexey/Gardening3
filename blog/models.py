from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=30)


class Review(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField
    estimation = models.PositiveSmallIntegerField()
