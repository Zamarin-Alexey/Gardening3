from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.messages import get_messages

from .models import *
from .forms import *


def show_plants(request, param):
    if param == 'all':
        plants = Plant.objects.all()
        images = ImagePlant.objects.all()
        return render(request, 'plants/show_plants.html', {'title': 'Библиотека растений', 'plants': plants,
                                                           'images': images})
    else:
        plants = request.user.extenduser.plants.all()
        return render(request, 'plants/show_my_plants.html', {'title': 'Мои растения', 'plants': plants})


def plant_page(request, plant_id=None):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, 'plants/plant_page.html', {'title': plant.title, 'plant': plant})

def add_plant(request):
    plant_id = request.GET.get('plant_id')
    user = User.objects.get(pk=request.user.id)
    try:
        user = user.extenduser.plants.get(pk=plant_id)
        messages.error(request, "Растение уже добавлено")
    except Plant.DoesNotExist:
        plant = Plant.objects.get(pk=plant_id)
        user.profile.plants.add(plant)
        messages.success(request, "Растение успешно добавлено")
    except Exception as e:
        messages.error(request, "Упс! Произошла ошибка. Повторите позже")
    mes = get_messages(request)
    response = {
                'is_taken': True,
                'messages': mes,
            }
    return JsonResponse(response)