from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.db.models import Q

from blog.forms import *
from blog.models import *


def home_page(request):
    search = request.GET.get('search')
    if search:
        posts = Post.objects.filter(Q(title__contains=search) | Q(body__contains=search) | Q(tags__contains=search))
    else:
        posts = Post.objects.all()
    return render(request, 'blog/home_page.html',
                  {'title': 'Блог', 'posts': posts, 'user': request.user})


def post_page(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = AddCommentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.user
            form.post_id = post
            form.save()
            return redirect(post)
    else:
        form = AddCommentForm()
        user = post.user
        images = Image.objects.filter(post=post.pk)
        profile = user.profile
        comments = Comment.objects.filter(post_id=post)
    return render(request, 'blog/post.html',
                  {'title': 'Пост#' + str(post_id), 'post': post, 'images': images, 'user': user, 'profile': profile,
                   'comments': comments, 'comment_form': form})


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(title=form.cleaned_data['title'],
                                       body=form.cleaned_data['body'].replace('\n', '<br />'),
                                       tags=form.cleaned_data['tags'],
                                       user=request.user)
            for f in request.FILES.getlist('images'):
                data = f.read()
                image = Image(post=post)
                image.image.save(f.name, ContentFile(data))
                image.save()
            return redirect(post)
    else:
        form = AddPostForm()
    return render(request, 'blog/add_post.html', {'title': 'Добавление поста', 'form': form})
