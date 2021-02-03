
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import DatosPersonales
from django.contrib.auth.models import User 
from .forms import RegistroPaciente, EditarUsuarioForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def usuario_permitido(usuario):
        if usuario.datospersonales.rol == 2:
            validacion = True
        else:
            validacion = False
        return validacion

class Registro(LoginRequiredMixin,UserPassesTestMixin,View):
    model = DatosPersonales
    form_class = RegistroPaciente
    template_name = 'app_admin/registro.html'
    success_url = 'app_admin:registro'

    def test_func(self):
        return usuario_permitido(self.request.user)

    def get(self, request):
        context = {
            'pacientes':self.get_pacientes(),
            'form':self.form_class
        }
        return render(request, self.template_name, context )
    
    def post(self, request):
        formulario = self.form_class(request.POST)
        if formulario.is_valid():
            data_post= formulario.cleaned_data
            print(data_post)
            
            try:
                user = User.objects.create_user(
                    username=data_post['username'] ,email='', password='1234',
                    first_name=data_post['nombre'], last_name=data_post['apellido']
                )

            except IntegrityError as e:
                print('fallo')
                messages.warning(request,"Error, El username ya se encuentra registrado")
                context = {
                    'pacientes':self.get_pacientes(),
                    'form':formulario
                }
                return render(request, self.template_name, context)

            DatosPersonales.objects.create(
                    usuario_id = user.id,
                    rol=data_post['rol']
                )
            messages.success(request,'Usuario Creado')

            return redirect(self.success_url)

    def get_pacientes(self):
        registro = DatosPersonales.objects.filter(rol=1)
        pacientes = []
        for row in registro:
            data = {}
            user = row.usuario_id
            dato = User.objects.get(id=user)
            data['datos_personales'] = row
            data['identidad'] = dato
            #print(dir(data['identidad']))
            pacientes.append(data)
        return pacientes


class BorrarUsuario(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = User
    template_name = "app_admin/delete.html"
    success_url = reverse_lazy('app_admin:registro')

    def test_func(self):
        return usuario_permitido(self.request.user)

    def delete(self, request, *args, **kwargs):
        id_user = self.kwargs['pk']
        User.objects.get(id=id_user).delete()
        return redirect(self.success_url)


