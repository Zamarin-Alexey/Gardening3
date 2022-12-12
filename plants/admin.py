from django.contrib import admin
from .models import *


class PhotoPlantInline(admin.TabularInline):
    model = PhotoPlant


class PlantAdmin(admin.ModelAdmin):
    inlines = [
        PhotoPlantInline,
    ]


admin.site.register(Plant, PlantAdmin)
