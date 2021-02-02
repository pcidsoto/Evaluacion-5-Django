from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
#from .models import Administrador, DatosPersonales


class RegistroPaciente(forms.Form):

    run = forms.CharField(
        label='R.U.N',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'9.999.999-9'},
            ),
        validators=[validators.MaxLengthValidator(12,'Rut Incorrecto!'),
                validators.MinLengthValidator(11,'Rut Incorrecto')]
        )
    nombre = forms.CharField(
        label='Nombre',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Ingrese su nombre'})
        )
    apellido_paterno = forms.CharField(
        label='Apellido Paterno',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Ingrese su apellido'})
        )
    apellido_materno = forms.CharField(
        label='Apellido Materno',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Ingrese su apellido'})
        )


class LoginForm(forms.Form):

    user = forms.CharField(
        label = 'Usuario',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su Usuario'
        })
    )

    password = forms.CharField(
        label = 'Contraseña',
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder':'Ingrese su contraseña'
        })
    )

'''
class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            }
        fields = ['nombre','apellido_paterno','apellido_materno','email','direccion','telefono']

'''