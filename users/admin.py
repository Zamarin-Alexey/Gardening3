from django.contrib import admin
from .models import Profile
from blog.models import Plant

admin.site.register(Profile)
admin.site.register(Plant)