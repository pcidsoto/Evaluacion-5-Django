'''
from django import forms
from django.conf import settings
import json
from app_admin.models import DatosPersonales, Medicamento

users = list(DatosPersonales.objects.select_related('id_usuario').all().values_list('id_usuario', 'id_usuario'))
class PacientesForm(forms.Form):
    pacientes = forms.CharField(
        label = False,
        widget = forms.Select(choices = users, attrs={'class':'form-select'})
    )


class AgregarForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        widgets = {
            #Select realiza lista desplegable
           'id_usuario': forms.Select(attrs={'class':'form-control'}),
            #DateInput boostrap
           'fecha': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
           'nombre': forms.TextInput(attrs={'class':'form-control'}),
           'hora': forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}),
           'dosis': forms.TextInput(attrs={'class':'form-control'})
        }
        fields = '__all__'
'''