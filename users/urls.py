from django.urls import path

from .views import *

urlpatterns = [
    path('reg/', registration, name='reg_form'),
    path('login/', user_login, name='login_form'),
    path('logout/', user_logout, name='logout_form'),
    path('profile/', profile, name='profile_form'),
    path('edit/', edit_profile, name='edit_profile_form')
]
