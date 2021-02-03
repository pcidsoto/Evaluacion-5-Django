
from django.urls import path
from . import views

app_name = 'app_admin'

urlpatterns = [
    path('registro/', views.Registro.as_view() , name='registro' ),
    #path('editar/<pk>/', views.Editar.as_view() , name='editar' ),
    path('borrar/<pk>/', views.BorrarUsuario.as_view() , name='borrar' ),
]
