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
    if UserPlant.objects.filter(plant=plant.pk).exists():
        response = {
            'is_taken': True,
            'message': 'Растение уже добавлено',
        }
    else:
        user_plant = UserPlant.objects.create(user=request.user, plant=plant)
        user_plant.save()
        stages = plant.plantstage_set.all()
        for stage in stages:
            UserPlantStage.objects.create(user_plant=user_plant, plant_stage=stage).save()
        UserPlantStage.objects.filter(user_plant=user_plant, plant_stage=stages.get(number_stage=1)).update(
            active_stage=True)
        response = {
            'is_taken': UserPlant.objects.filter(plant=plant.pk, user=request.user.pk).exists(),
            'message': 'Растение добавлено успешно',
        }
    return JsonResponse(response)


def my_plant(request):
    plants = UserPlant.objects.filter(user_id=request.user.pk)

    return render(request, 'plants/show_myplants.html', {'title': 'Мои растения', 'plants': plants})


def my_plant_page(request, plant_id=None):
    plant = get_object_or_404(UserPlant, pk=plant_id)

    return render(request, 'plants/my_plant_page.html', {'title': f'{plant.plant.title} | {request.user}',
                                                         'plant': plant,
                                                         'stages': plant.userplantstage_set.all()})
