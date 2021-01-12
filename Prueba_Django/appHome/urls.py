from django.urls import path
from . import views

app_name = 'appHome'

urlpatterns = [
    path('home/', views.home, name="Home"),
]
