from django.shortcuts import render, redirect

from blog import models
from blog.forms import *


def home_page(request):
    posts = Post.objects.all()
    return render(request, 'blog/home_page.html', {'title': 'Блог', 'posts': posts})


def post_page(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/post.html', {'title': 'Пост#' + str(post_id), 'post': post})


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('blog_home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()
    return render(request, 'blog/add_post.html', {'title': 'Добавление поста', 'form': form})
