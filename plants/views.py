from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from .models import *
from .forms import *


def show_plants(request, param):
    if param == 'all':
        plants = Plant.objects.all()
        photos = PhotoPlant.objects.get
        return render(request, 'plants/show_plants.html', {'title': 'Библиотека растений', 'plants': plants,
                                                           'photos': photos})
    else:
        plants = request.user.profile.plants.all()
        return render(request, 'plants/show_my_plants.html', {'title': 'Мои растения', 'plants': plants})


def plant_page(request, plant_id=None):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, 'plants/plant_page.html', {'title': plant.title, 'plant': plant})


def add_plant(request):

    plant_id = int(request.GET.get('plant_id'))
    plant = Plant.objects.get(pk=plant_id)
    user = request.user
    if user.profile.plants.filter(pk=1).exists():
        response = {
            'is_taken': True,
            'message': 'Растение уже добавлено',
        }
    else:
        # user.profile.plants.add(plant)
        # user_plant = user.profile.plants.get(id=plant_id)
        # # stages = plant.plantstage_set.all()
        # for i in range(plant.plantstage_set.count()):
        #     UserPlantStage.objects.create(user=user, plant=plant).save()
        # UserPlantStage.objects.filter(user=user, plant=plant, =stages.get(
        #     number_stage=1)).update(
        #     active_stage=True)
        response = {
            'is_taken': True,#bool(user_plant),
            'message': 'Растение добавлено успешно',
        }
    return JsonResponse(response)


def my_plant_page(request, plant_id=None):
    plant = get_object_or_404(request.user.profile.plants, id=plant_id)
    stages = plant.userplantstage_set.all()

    return render(request, 'plants/my_plant_page.html', {'title': f'{plant.title} | {request.user.username}',
                                                         'plant': plant,
                                                         'stages': stages})


def stage_complete(request):
    # value - массив с растением и номером стадии
    if request.method == 'POST':
        form = CompleteStageForm(request.POST)
        if form.is_valid():
            user = request.user
            plant_id = request.POST.get('plant_id')
            num_stage = request.POST.get('num_stage')
            stages = user.userplantstage_set.objects.filter(plant=plant_id)
            request.user.objects.select_for_update()




