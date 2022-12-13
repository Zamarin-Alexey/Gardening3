from django.urls import path

from .views import *

urlpatterns = [
    path('', show_plants, name='plants'),
    path('plant/<int:plant_id>', plant_page, name='plant_page'),
    path('add_plant/', add_plant, name='add_plant'),
    path('my_plant/', my_plant, name='my_plant'),
]
