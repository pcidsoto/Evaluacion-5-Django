from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from .models import DatosPersonales

STATUS_CHOICES = (
            (1, "PACIENTE"),
            (2, "ADMIN"),
            (3, "MEDICO"),
            (4, "FAMILIAR"),
            (5, "CUIDADOR")
   )

class RegistroPaciente(forms.Form):
    username = forms.CharField(
        label='Username',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Nombre de usuario'})
        )

    nombre = forms.CharField(
        label='Nombre',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Ingrese su nombre'})
        )
    apellido = forms.CharField(
        label='Apellido',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Ingrese su apellido'})
        )
    rol = forms.ChoiceField(label='Rol', choices=STATUS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))



class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        fields = ['fecha_nacimiento','direccion','telefono','rol']

