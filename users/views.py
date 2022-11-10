from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/blog')
        # else:
        # messages.error(request, 'Error')
    else:
        form = UserCreationForm()

    return render(request, 'users/registration.html', {'title': 'Регистрация', 'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/blog')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'title': 'Авторизация', 'form': form})

def user_logout(request):
    logout(request)
    return redirect('../login')
