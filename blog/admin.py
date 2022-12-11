from django.contrib import admin

from .models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish_date', 'user_id')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'body')


admin.site.register(Post, PostsAdmin)
admin.site.register(Comment)
