from django import forms


class RegistroPaciente(forms.Form):

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
    fecha_nacimiento = forms.DateField(
        label='Fecha de nacimiento',
        widget= forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder':'Año-Mes-Dia'})
        )

