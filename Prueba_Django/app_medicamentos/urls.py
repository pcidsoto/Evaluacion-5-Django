from django.urls import path

from . import views

app_name='app_medicamentos'
urlpatterns = [
    path( 'medicamentos', views.app_medicamentos, name='medicamentos')
]
