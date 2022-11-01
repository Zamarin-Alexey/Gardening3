from django.contrib import admin
from django.urls import path, include
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('users/', include('users.urls'))
]
