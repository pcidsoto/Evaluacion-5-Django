from django import forms
from django.conf import settings
from app_admin.models import Usuarios, DatosPersonales


class PacientesForm(forms.ModelForm):
    class Meta:        
        model = DatosPersonales
        
        fields = ['id_usuario']

        def __init__(self, *args, **kwargs):
            super(PacientesForm, self).__init__(*args, **kwargs)
            self.fields['id_usuario'] = forms.ModelChoiceField(
                queryset=DatosPersonales.objects.select_related('id_usuario').all(),
                widget=forms.Select(attrs={'class': 'form-control'}))


class EditarDatosForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'})
        }
        fields = ['nombre','apellido_paterno','apellido_materno','direccion',
            'email','telefono']
