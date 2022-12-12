from django.urls import path

from .views import *

urlpatterns = [
    path('plants/', show_plants, name='plants'),
    path('plant/<int:plant_id>', plant_page, name='plant'),
]
