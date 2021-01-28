from django import forms
from django.conf import settings
from app_admin.models import Usuarios, DatosPersonales
import json 

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

users = DatosPersonales.objects.select_related('id_usuario').all().values_list('id_usuario', 'id_usuario')
class Pacientes(forms.Form):
    pacientes = forms.CharField(
        label = False,
        widget = forms.Select(choices = users, attrs={'class':'form-select'})
    )

'''class PacientesForm(forms.ModelForm):
    class Meta:        
        model = DatosPersonales
        fields = ['id_usuario']

        def __init__(self, *args, **kwargs):
            super(PacientesForm, self).__init__(*args, **kwargs)
            self.fields['id_usuario'] = forms.ModelChoiceField(
                queryset=DatosPersonales.objects.select_related('id_usuario').all(),
                widget=forms.Select(attrs={'class': 'form-control'}))
            print(DatosPersonales.objects.select_related('id_usuario').all())'''