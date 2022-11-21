from django.urls import path

from .views import *

urlpatterns = [
    path('', home_page, name='blog_home'),
    path('post/<int:post_id>', post_page, name='post'),
]
