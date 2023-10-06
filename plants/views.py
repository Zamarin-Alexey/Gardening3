import datetime

from django.db.models import Avg, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from users.models import ExtendUser
from .models import *
from .forms import *


def calc_rating(plant):
    reviews = Review.objects.filter(plant=plant)
    if reviews:
        new_rating = int(reviews.aggregate(Avg('estimation')).get('estimation__avg'))
    else:
        new_rating = 0
    return new_rating


def show_plants(request, param):
    if param == 'all':
        search = request.GET.get('search')
        if search:
            plants = Plant.objects.filter(
                Q(title__contains=search) | Q(review__body__contains=search) | Q(tags__contains=search))
        else:
            plants = Plant.objects.all()
        return render(request, 'plants/show_plants.html', {'title': 'Библиотека растений', 'plants': plants})
    else:
        plants = request.user.extenduser.plants.all()
        return render(request, 'plants/show_my_plants.html', {'title': 'Мои растения', 'plants': plants})


def plant_page(request, plant_id=None):
    plant = get_object_or_404(Plant, pk=plant_id)
    form = ReviewForm()
    reviews = Review.objects.filter(plant=plant)
    images = ImagePlant.objects.filter(plant=plant)
    return render(request, 'plants/plant_page.html',
                  {'title': plant.title, 'plant': plant, 'form': form, 'reviews': reviews, 'images': images})


@login_required
def add_plant(request):
    plant_id = request.GET.get('plant_id')
    user = User.objects.get(pk=request.user.id)
    try:
        user = user.extenduser.plants.get(pk=plant_id)
        message = "Растение уже добавлено"
    except Plant.DoesNotExist:
        plant = Plant.objects.get(pk=plant_id)
        user.extenduser.plants.add(plant)
        message = "Растение успешно добавлено"
    except Exception as e:
        message = "Упс! Произошла ошибка. Повторите позже"
    response = {
        'messages': message,
    }
    return JsonResponse(response)


def add_review(request, plant_id):
    is_taken = False
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                plant = Plant.objects.get(pk=plant_id)
                review = form.save(commit=False)
                review.user = request.user
                review.plant = plant
                review.published_date = datetime.datetime.now()
                review.save()
                rating = calc_rating(plant)
                Plant.objects.filter(pk=plant_id).update(rating=rating)
                is_taken = True
            except Exception as e:
                print(e)
    else:
        form = ReviewForm()
    response = {
        'is_taken': is_taken,
    }
    return redirect(f'/plants/plant/{plant_id}')


def delete_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    plant = review.plant
    if request.user.pk == review.user.pk:
        try:
            review = Review.objects.get(pk=review_id)
            plant = review.plant
            review.delete()
            messages.success(request, 'Рецензия удалена успешно')
            rating = calc_rating(plant)
            Plant.objects.filter(pk=plant.id).update(rating=rating)
        except Exception as e:
            messages.error(request, 'Упс! Произошла ошибка. Повторите позже')


    else:
        messages.error(request, 'У вас нет доступа')
    return redirect(f'/plants/plant/{plant.pk}')


def like_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    extend_user = ExtendUser.objects.get(user=User.objects.get(pk=request.user.pk))
    like_exist = extend_user.liked_reviews.filter(pk=review.pk)
    if not like_exist:
        review.likes += 1
        extend_user.liked_reviews.add(review)
    else:
        review.likes -= 1
        extend_user.liked_reviews.remove(review)
    review.save()
    extend_user.save()
    return redirect(review.plant)
