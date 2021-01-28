from django import forms
from django.conf import settings
import json
from app_admin.models import DatosPersonales

users = list(DatosPersonales.objects.select_related('id_usuario').all().values_list('id_usuario', 'id_usuario'))
class PacientesForm(forms.Form):
    pacientes = forms.CharField(
        label = False,
        widget = forms.Select(choices = users, attrs={'class':'form-select'})
    )

