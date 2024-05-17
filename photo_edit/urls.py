from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("edit", views.edit_image, name='photoedit'),
]
