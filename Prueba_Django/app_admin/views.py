'''
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
#from .models import Administrador, Usuarios, DatosPersonales
from .forms import RegistroPaciente, LoginForm, EditarUsuarioForm


class Login(View):
    form_class = LoginForm
    template_name = "app_admin/login.html"
    success_url = 'app_admin:registro'

    def get(self, request):
        formulario = self.form_class
        context = {'form': formulario}
        return render(request, self.template_name, context)

    def post(self, request):
        formulario = self.form_class(request.POST) 
        if formulario.is_valid():
            form_data = formulario.cleaned_data
            login_user = Administrador.objects.filter(usuario=form_data['user']).values_list()
            if not login_user:
                messages.success(request, 'Usuario o Contraseña Incorrecta')
                context = {'form': formulario}
                return render(request, 'app_admin/login.html', context)

            if form_data['user']==login_user[0][0] and form_data['password']==login_user[0][1]:
                return redirect(self.success_url)
            else:
                messages.success(request, 'Usuario o Contraseña Incorrecta')
                context = {'form': formulario}
                return render(request, 'app_admin/login.html', context)


class Registro(CreateView):
    model = DatosPersonales
    form_class = RegistroPaciente
    template_name = 'app_admin/registro.html'
    success_url = 'app_admin:registro'

    def get(self, request):
        registros = Usuarios.objects.all().values()
        datos = DatosPersonales.objects.select_related('id_usuario').all().values()
        data = Usuarios.objects.all().values()
        context = {'form': self.form_class, 'registros': datos }
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        data_post = self.form_class(request.POST)
        if data_post.is_valid():
            data_post = data_post.cleaned_data
            try:
                usuario_nuevo = Usuarios.objects.create(
                    usuario=data_post['run'],
                    contraseña='12345'
                )
            except IntegrityError as e:
                messages.warning(request,"Error, El rut ya se encuentra registrado")
                return redirect(self.success_url)

            DatosPersonales.objects.create(
                id_usuario=usuario_nuevo,
                nombre = data_post['nombre'],
                apellido_paterno = data_post['apellido_paterno'],
                apellido_materno = data_post['apellido_materno'],
            )
            messages.success(request,'Usuario Creado')
            return redirect(self.success_url)
        else:
            datos = DatosPersonales.objects.select_related('id_usuario').all().values()
            context = {'form': data_post, 'registros': datos }
            return render(request, self.template_name, context=context)


class Editar(UpdateView):
    model = DatosPersonales
    form_class = EditarUsuarioForm
    template_name = 'app_admin/edit.html'
    success_url = reverse_lazy('app_admin:registro')


class BorrarUsuario(DeleteView):
    model = DatosPersonales
    template_name = "app_admin/delete.html"
    success_url = reverse_lazy('app_admin:registro')

    def delete(self, request, *args, **kwargs):
        id_user = self.kwargs['pk']
        user = DatosPersonales.objects.select_related('id').filter(id=id_user).values_list()[0]
        Usuarios.objects.get(usuario=user[1]).delete()
        return redirect(self.success_url)


'''