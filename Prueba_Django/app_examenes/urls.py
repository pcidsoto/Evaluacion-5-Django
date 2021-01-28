from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'app_examenes'

urlpatterns = [
    path('', views.ExamenesView.as_view(), name='examen'),
]
