from django import forms
from django.conf import settings
import json

from app_admin.models import Hemograma, DatosPersonales, PerfilLipidico


users = DatosPersonales.objects.select_related('id_usuario').all().values_list('id_usuario', 'id_usuario')

class PacientesFormSelect(forms.Form):
    pacientes = forms.CharField(
        label = False,
        widget = forms.Select(choices = users, attrs={'class':'form-select'})
    )


class HemogramaForm(forms.ModelForm):
    class Meta:
        model = Hemograma
        widgets = {
                'id_usuario': forms.Select(attrs={'class':'form-control'}),
                'fecha': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
                'hematocrito': forms.NumberInput(attrs={'class': 'form-control'}),
                'hemoglobina': forms.NumberInput(attrs={'class': 'form-control'}),
                'rcto_eritrocitos': forms.NumberInput(attrs={'class': 'form-control'}),
                'rcto_leucocitos': forms.NumberInput(attrs={'class': 'form-control'}),
                'rcto_plaquetas': forms.NumberInput(attrs={'class': 'form-control'}),
                'v_c_m': forms.NumberInput(attrs={'class': 'form-control'}),
                'h_c_m': forms.NumberInput(attrs={'class': 'form-control'}),
                'c_h_c_m': forms.NumberInput(attrs={'class': 'form-control'}),
                'r_d_w_c_v': forms.NumberInput(attrs={'class': 'form-control'}),
                'serie_roja': forms.TextInput(attrs={'class': 'form-control'}),
                'serie_blanca': forms.TextInput(attrs={'class': 'form-control'}),
                'plaquetas': forms.TextInput(attrs={'class': 'form-control'}),
                }
        fields = '__all__'
        
class PerfilLipidicoForm(forms.ModelForm):
    class Meta:
        model = PerfilLipidico
        widgets = {
                'id_usuario': forms.Select(attrs={'class':'form-control'}),
                'fecha': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
                'glicemia': forms.NumberInput(attrs={'class': 'form-control'}),
                'hdl_colesterol': forms.NumberInput(attrs={'class': 'form-control'}),
                'ldl_colesterol': forms.NumberInput(attrs={'class': 'form-control'}),
                'colesterol_total': forms.NumberInput(attrs={'class': 'form-control'}),
                'trigliceridos': forms.NumberInput(attrs={'class': 'form-control'}),
                'colesterol_total_hdl': forms.NumberInput(attrs={'class': 'form-control'}),
                }
        fields = '__all__'



