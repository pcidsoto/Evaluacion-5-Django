from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'app_examenes'

urlpatterns = [
    path('examenes/', views.index, name="examenes"),
    path('examenes/', TemplateView.as_view(template_name='app_examenes/examenes.html'), name='examenes'),

]
