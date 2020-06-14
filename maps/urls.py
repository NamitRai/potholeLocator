from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.default_map, name="default"),
    path('about/', views.about, name="about"),
]
