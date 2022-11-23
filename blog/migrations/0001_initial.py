# Generated by Django 4.1.3 on 2022-11-22 13:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('planting_period', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_start', models.DateField(auto_now=True)),
                ('plant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.plant')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('estimation', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('image', models.ImageField(upload_to='images/')),
                ('tags', models.CharField(max_length=255)),
                ('plant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.plant')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Текст поста')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Изображение')),
                ('tags', models.CharField(blank=True, max_length=255, verbose_name='Теги')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-publish_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('publish_date', models.DateTimeField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]