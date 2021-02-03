from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic import View, ListView
#from .forms import PacientesForm, EditarDatosForm
from app_admin.models import DatosPersonales
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

    
 

class Home(LoginRequiredMixin,UserPassesTestMixin, View):
    template_name = 'app_home/home.html'
    success_url = 'app_home:Home'
    
    def test_func(self):
        return self.usuario_permitido(self.request.user)

    def get(self, request, **kwargs):
        return render(request, self.template_name)

    def usuario_permitido(self, usuario):
        if usuario.datospersonales.rol == 2 or usuario.datospersonales.rol == 1:
            validacion = True
        else:
            validacion = False
        return validacion 
    

'''
class EditarDatosPersonales(View):
    model = DatosPersonales
    form_class = EditarDatosForm
    template_name = 'app_home/edit.html'
    success_url = 'app_home:Home'

    def get(self, request, pk):
        #print(pk)
        datos_paciente = self.model.objects.filter(id=pk).values()[0]
        #print(datos_paciente)
        formulario = self.form_class(initial=datos_paciente)
        #print(formulario)
        context = {'form': formulario, 'id':pk}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        print(pk)
        formulario = self.form_class(request.POST) 
        if formulario.is_valid():
            form_data = formulario.cleaned_data
            print(form_data)
            self.model.objects.filter(id=pk).update(
                            nombre = form_data['nombre'],
                            apellido_paterno = form_data['apellido_paterno'],
                            apellido_materno = form_data['apellido_materno'],
                            direccion = form_data['direccion'],
                            email = form_data['email'],
                            telefono = form_data['telefono']
                            )
            return redirect(self.success_url)
        else:
            print('no valido')
            return render(request, self.template_name, {'form': formulario})'''