from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from blog.forms import *
from blog.models import *
from users.models import *


def home_page(request, category='popular', prev_search=None):
    search = request.GET.get('search')
    if search:
        founded_posts = Post.objects.filter(
            Q(title__contains=search) | Q(body__contains=search) | Q(tags__contains=search))
    elif prev_search:
        search = prev_search
        founded_posts = Post.objects.filter(
            Q(title__contains=search) | Q(body__contains=search) | Q(tags__contains=search))
    else:
        founded_posts = Post.objects.all()
    if category == 'popular':
        posts = founded_posts.order_by('-likes')[:5]
    elif category == 'my':
        posts = founded_posts.filter(user=request.user)
    else:
        posts = founded_posts

    return render(request, 'blog/home_page.html',
                  {'title': 'Блог', 'posts': posts, 'user': request.user, 'category': category, 'search': search})


def post_page(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = AddCommentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = post
            form.save()
            return redirect(post)
    else:
        form = AddCommentForm()
        user = post.user
        images = Image.objects.filter(post=post.pk)
        profile = user.profile
        comments = Comment.objects.filter(post_id=post)
    return render(request, 'blog/post.html',
                  {'title': f"{post.title} | {user.username}", 'post': post, 'images': images, 'user': user, 'profile':
                      profile,
                   'comments': comments, 'comment_form': form})


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            for f in request.FILES.getlist('images'):
                data = f.read()
                image = Image(post=post)
                image.image.save(f.name, ContentFile(data))
                image.save()
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html',
                  {'title': 'Добавление поста', 'form': form})


def edit_post(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            for f in request.FILES.getlist('images'):
                data = f.read()
                image = Image(post=post)
                image.image.save(f.name, ContentFile(data))
                image.save()
            messages.success(request, 'Изменения сохранены')
            return redirect(post)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'title': 'Редактирование поста', 'form': form, 'post': post})


def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/')


def like_post(request, post_id, user_id):
    post = Post.objects.get(pk=post_id)
    extend_user = ExtendUser.objects.get(user=User.objects.get(pk=user_id))
    like_exist = extend_user.liked_posts.filter(pk=post.pk)
    if not like_exist:
        post.likes += 1
        extend_user.liked_posts.add(post)
    else:
        post.likes -= 1
        extend_user.liked_posts.remove(post)
    post.save()
    extend_user.save()
    return redirect(post)


def global_search(request, category='popular', prev_search=None):
    search = request.GET.get('global_search')
    if not search:
        search = prev_search

    posts, users, plants = None, None, None

    if category == 'posts':
        posts = Post.objects.filter(
            Q(title__contains=search) | Q(body__contains=search) | Q(tags__contains=search))
    elif category == 'plants':
        plants = Post.objects.filter(
            Q(title__contains=search) | Q(body__contains=search) | Q(tags__contains=search))
    else:
        users = Post.objects.filter(
            Q(title__contains=search) | Q(body__contains=search) | Q(tags__contains=search))

    return render(request, 'blog/search_page.html',
                  {'title': 'Блог', 'posts': posts, 'users': users, 'plants': plants, 'user': request.user,
                   'category': category, 'search': search})
