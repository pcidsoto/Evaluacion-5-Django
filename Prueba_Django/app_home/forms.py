from django import forms
from django.conf import settings
import json
from app_admin.models import Usuarios
from app_admin.models import DatosPersonales

class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno' : forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno' : forms.TextInput(attrs={'class': 'form-control'})
        }
        #fields = '__all__'
        fields = ['nombre', 'apellido_paterno', 'apellido_materno']









filename = '/data/data_registros.json'

def leer_pacientes(filename, settings):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)
    print(pacientes)
    lista_pacientes= [('-------','--------')]
    
    for elemento in pacientes['pacientes']:
        for clave in elemento.keys():

            lista_pacientes.append((clave,clave))
    return lista_pacientes

users = leer_pacientes(filename, settings)
class Pacientes(forms.Form):
    pacientes = forms.CharField(
        label = False,
        widget = forms.Select(choices = users, attrs={'class':'form-select'})
    )

