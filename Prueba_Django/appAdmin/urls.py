from django.urls import path
from . import views

app_name = 'appAdmin'

urlpatterns = [
    path('registro/', views.registro, name='registro' )
]
