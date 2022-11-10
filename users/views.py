from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def login(request):
    return render(request, 'users/login.html', {'title': 'Авторизация'})


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login)
        # else:
        # messages.error(request, 'Error')
    else:
        form = UserCreationForm()

    return render(request, 'users/registration.html',
                  {'title': 'Регистрация', 'form': form})
