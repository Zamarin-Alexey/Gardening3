from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


from .forms import UpdateUserForm
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
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
            return render(request, 'home_page.html')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'title': 'Авторизация', 'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    #return render(request, 'users/profile.html')
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        #profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid(): # and profile_form.is_valid():
            user_form.save()
            # profile_form.save()
            # messages.success(request, 'Your profile is updated successfully')
            return redirect(profile)
    else:
        user_form = UpdateUserForm(instance=request.user)
        # profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form}) # , 'profile_form': profile_form})

