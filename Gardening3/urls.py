from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Gardening3 import settings
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
