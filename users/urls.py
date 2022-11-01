from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login, name='login_form'),
    path('reg/', registration, name='reg_form'),
]
