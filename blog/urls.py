from django.urls import path

from .views import *

urlpatterns = [
    path('', home_page, name='blog_home'),
    path('post/<int:post_id>', post_page, name='post'),
    path('add_post/', add_post, name='add_post'),
    path('edit_post/<int:post_id>', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>', delete_post, name='delete_post'),
    path('post/<int:post_id>/<int:user_id>', like_post, name='like_post'),
    path('category/<str:category>/<str:prev_search>', home_page, name='category')
]
