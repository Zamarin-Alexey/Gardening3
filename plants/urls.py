from django.urls import path, re_path

from .views import *

urlpatterns = [
    re_path(r'(all|my-plant)', show_plants, name='plants'),
    path('plant/<int:plant_id>', plant_page, name='plant_page'),
    path('add_plant/', add_plant, name='add_plant'),
    #path('my_plant/', my_plant, name='my_plant'),
    path('my_plant/<int:plant_id>', my_plant_page, name='my_plant_page'),
]
