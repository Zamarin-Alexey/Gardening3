from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from .models import *
from .forms import *


def show_plants(request):
    plants = Plant.objects.all()

    photos = PhotoPlant.objects.get
    return render(request, 'plants/show_plants.html', {'title': 'Библиотека растений', 'plants': plants,
                                                       'photos': photos})


def plant_page(request, plant_id=None):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, 'plants/plant_page.html', {'title': plant.title, 'plant': plant})


def add_plant(request):
    plant_id = request.GET.get('plant_id')
    plant = Plant.objects.get(pk=plant_id)
    if not UserPlant.objects.filter(plant=plant.pk).exists():
        user_plant = UserPlant()
        user_plant.title = plant.title
        user_plant.date_finish = plant.period_finish-plant.period_start + datetime.date.today()
        user_plant.user = request.user
        user_plant.plant = plant
        user_plant.save()
        response = {
            'is_taken': UserPlant.objects.filter(plant=plant.pk, user=request.user.pk).exists(),
            'message': 'Растение добавлено успешно',
        }
    else:
        response = {
            'is_taken': True,
            'message': 'Растение уже добавлено',
        }
    return JsonResponse(response)

def my_plant(request):
    plants = UserPlant.objects.filter(user_id=request.user.pk)

    return render(request, 'plants/show_myplants.html', {'title': 'Мои растения', 'plants': plants})