from django.contrib import admin
from .models import *


class ImagePlantInline(admin.TabularInline):
    model = ImagePlant


class PlantAdmin(admin.ModelAdmin):
    inlines = [
        ImagePlantInline
    ]


admin.site.register(Plant, PlantAdmin)
admin.site.register(Category)
