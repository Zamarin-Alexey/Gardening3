import django.http
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse, HttpResponse

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


@login_required
def profile(request, user_name=None):
    user = get_object_or_404(User, username=user_name)

    user_form = UpdateUserForm(instance=user)
    profile_form = UpdateProfileForm(instance=user.profile)
    return render(request, 'users/profile.html', {'title': user.username, 'user': user,
                                                  'profile': user.profile,
                                                  'user_form': user_form,
                                                  'profile_form': profile_form})


def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Изменения сохранены')
            return redirect(profile)
    else:
        user = request.user
        user_form = UpdateUserForm(instance=user)
        profile_form = UpdateProfileForm(instance=user.profile)
    return render(request, 'users/profile.html', {'title': user.username, 'user': user,
                                                  'profile': user.profile,
                                                  'user_form': user_form,
                                                  'profile_form': profile_form})



def validate_username(request):
    username = request.GET.get('username')
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)
