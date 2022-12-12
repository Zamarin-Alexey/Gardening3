from django.contrib import admin
from .models import Profile



class ProfileInline(admin.TabularInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]
