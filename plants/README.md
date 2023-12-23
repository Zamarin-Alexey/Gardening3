# Микросервис Plant #

МК Plant отвечает за обработку запросов пользователей на получение информации о растениях.

Для интеграции МК в систему необходимо:

1) Склонировать папку в свой проект: *app/plants*
2) Прописать url в *app/app/urls.py*

```
urlpatterns = [ 
        ... 
        path('plants/', include('plants.urls')),
]
```

3) Добавить приложение в *app/app/settings.py*

```
INSTALLED_APPS = [
    ...
    'plants.apps.PlantsConfig',
    ...
]
```
4) Выполнить создание миграций

```
python manage.py makemigrations plants <others your models> 
python manage.py migrate
```
5) Запустить сервер