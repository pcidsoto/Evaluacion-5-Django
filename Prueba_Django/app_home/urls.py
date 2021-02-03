from django.urls import path
from . import views

app_name = 'app_home'

urlpatterns = [
    path('home/', views.Home.as_view(), name="Home"),
    #path('editar/<slug:pk>/', views.EditarDatosPersonales.as_view() , name="editar"),
]
