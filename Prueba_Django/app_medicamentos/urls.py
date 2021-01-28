from django.urls import path, include
from django.contrib import admin
from . import views


app_name='app_medicamentos'
urlpatterns = [
    path( '', views.MedicamentoView.as_view(), name='medicamentos')
]

