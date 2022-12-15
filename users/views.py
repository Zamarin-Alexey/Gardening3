import django.http
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse

from .forms import UpdateUserForm, UpdateProfileForm
from .forms import *


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('blog_home')
            except:
                form.add_error(None, 'Ошибка регистрации')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/registration.html', {'title': 'Регистрация', 'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'title': 'Авторизация', 'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')


def profile(request, user_id):
    user = User.objects.get(pk=user_id)

    is_owner = (request.user == user)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Изменения сохранены')
            return redirect(profile)
    else:
        user_form = UpdateUserForm(instance=user)
        profile_form = UpdateProfileForm(instance=user.profile)
    return render(request, 'users/profile.html',
                  {'title': user.username, 'user': {'username': user.username, 'email': user.email},
                   'profile': user.profile,
                   'user_form': user_form,
                   'profile_form': profile_form,
                   'is_owner': is_owner
                   })


def validate_username(request):
    username = request.GET.get('username')
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)


@login_required
def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('/')