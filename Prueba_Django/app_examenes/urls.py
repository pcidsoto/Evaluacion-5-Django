from django.urls import path
from . import views

app_name = 'app_examenes'

urlpatterns = [
    #path('', views.examenes, name='examen'),
    path('', views.ExamenesView.as_view(), name='examen'),
    path('agregar_hemograma/<pk>/', views.AgregarHemograma.as_view(), name='add_hemo'),
    path('agregar_perfillipidico/<pk>/', views.AgregarPerfilLipidico.as_view(), name='add_plip'),

]
