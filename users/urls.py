from django.urls import path

from .views import *

urlpatterns = [
    path('reg/', registration, name='reg_form'),
    path('login/', user_login, name='login_form'),
    path('logout/', user_logout, name='logout_form'),
    path('profile/<int:user_id>', profile, name='profile_form'),
    path('reg/validate_username/', validate_username, name='validate_username'),
    path('delete_user/<int:user_id>', delete_user, name='delete_user')
]
