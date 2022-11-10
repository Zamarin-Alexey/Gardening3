from django.urls import path

from .views import *

urlpatterns = [
    path('reg/', registration, name='reg_form'),
    path('login/', user_login, name='login_form'),
    path('logout/', user_logout, name='logout_form'),
]
