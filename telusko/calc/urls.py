from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.calc, name='calc'),
    path('jod', views.jod, name='jod')
]
