from django.shortcuts import render

from blog import models


def home_page(request):
    posts = models.Post.objects.all()
    return render(request, 'blog/home_page.html', {'title': 'Блог', 'posts': posts})


def post_page(request, post_id):
    post = models.Post.objects.get(pk=post_id)
    return render(request, 'blog/post.html', {'title': 'Блог', 'post': post})
