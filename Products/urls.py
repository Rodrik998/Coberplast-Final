from django.contrib import admin
from django.urls import path

from Products.views import simple_upload

urlpatterns = [
    path('crear-producto/', simple_upload, name="crear_producto"),
] 
