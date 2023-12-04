from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from Base_App.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='inicio')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
