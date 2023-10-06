from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

class ProfileInline(admin.TabularInline):
    model = Profile


class CustomUserAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)