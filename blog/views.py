import PIL
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile

from blog.forms import *
from blog.models import *


def home_page(request):
    posts = Post.objects.all()

    return render(request, 'blog/home_page.html',
                  {'title': 'Блог', 'posts': posts, 'user': request.user})


def post_page(request, post_id):
    post = Post.objects.get(pk=post_id)
    images = Image.objects.filter(post=post.pk)
    return render(request, 'blog/post.html', {'title': 'Пост#' + str(post_id), 'post': post, 'images': images})


def add_post(request):

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(title=form.cleaned_data['title'],
                                       body=form.cleaned_data['body'],
                                       tags=form.cleaned_data['tags'],
                                       user_id=request.user)
            for f in request.FILES.getlist('images'):
                data = f.read()
                image = Image(post=post)
                image.image.save(f.name, ContentFile(data))
                image.save()
            return redirect(post)
    else:
        form = AddPostForm()
    return render(request, 'blog/add_post.html', {'title': 'Добавление поста', 'form': form})
