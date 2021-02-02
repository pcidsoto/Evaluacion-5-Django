'''
from django import forms
from django.conf import settings
import json

from app_admin.models import Hemograma, DatosPersonales, PerfilLipidico, PresionArterial, PerfilBioquimico


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

class PerfilBioquimicoForm(forms.ModelForm):
    class Meta:
        model = PerfilBioquimico
        widgets = {
                'id_usuario': forms.Select(attrs={'class':'form-control'}),
                'fecha': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
                'glucosa': forms.NumberInput(attrs={'class': 'form-control'}),
                'nitrogeno_ureico': forms.NumberInput(attrs={'class': 'form-control'}),
                'urea': forms.NumberInput(attrs={'class': 'form-control'}),
                'acido_urico': forms.NumberInput(attrs={'class': 'form-control'}),
                'colesterol_total': forms.NumberInput(attrs={'class': 'form-control'}),
                'proteinas_totales': forms.NumberInput(attrs={'class': 'form-control'}),
                'albumina': forms.NumberInput(attrs={'class': 'form-control'}),
                'globulina': forms.NumberInput(attrs={'class': 'form-control'}),
                'bilirrubina_total': forms.NumberInput(attrs={'class': 'form-control'}),
                'transaminasa_gpt_alt': forms.NumberInput(attrs={'class': 'form-control'}),
                'transaminasa_got_ast': forms.NumberInput(attrs={'class': 'form-control'}),
                'g_glutamiltransferasa': forms.NumberInput(attrs={'class': 'form-control'}),
                'deshidrogenasa_lactica': forms.NumberInput(attrs={'class': 'form-control'}),
                'fosfatasas_alcalinas': forms.NumberInput(attrs={'class': 'form-control'}),
                'calcio': forms.NumberInput(attrs={'class': 'form-control'}),
                'fosforo': forms.NumberInput(attrs={'class': 'form-control'}),
                }
        fields = '__all__'
        
        
class PresionArterialForm(forms.ModelForm):
    class Meta:
        model = PresionArterial
        widgets = {
                'id_usuario': forms.Select(attrs={'class':'form-control'}),
                'fecha': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
                'presion_diatolica_mañana': forms.NumberInput(attrs={'class': 'form-control'}),
                'presion_sistolica_mañana': forms.NumberInput(attrs={'class': 'form-control'}),
                'presion_diatolica_tarde': forms.NumberInput(attrs={'class': 'form-control'}),
                'presion_sistolica_tarde': forms.NumberInput(attrs={'class': 'form-control'})
                }
        fields = '__all__'



'''
