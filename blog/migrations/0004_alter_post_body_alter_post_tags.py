# Generated by Django 4.1.3 on 2022-11-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='Текст поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=255, verbose_name='Теги'),
        ),
    ]
