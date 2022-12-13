from django.urls import path

from .views import *

urlpatterns = [
    path('reg/', registration, name='reg_form'),
    path('login/', user_login, name='login_form'),
    path('logout/', user_logout, name='logout_form'),
    # path('profile/', profile, name='profile_form'),
    path('profile/<str:user_name>', profile, name='profile_pk'),
    path('edit/', edit_profile, name='edit_profile_form'),
    path('reg/validate_username/', validate_username, name='validate_username')
]
