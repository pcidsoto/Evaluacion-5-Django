from django.shortcuts import render, redirect
from django.conf import settings
from .forms import LoginForm
import json

#from app_admin.models import Usuarios
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib import messages
'''
class Login(View):
    form_class = LoginForm
    template_name = "app_principal/index.html"
    success_url = 'app_home:Home' #revisar al momento de hacer el merge

    def get(self, request):
        formulario = self.form_class
        context = {'form': formulario}
        return render(request, self.template_name, context)

    def post(self, request):
        formulario = self.form_class(request.POST)
        
        if formulario.is_valid():
            form_data = formulario.cleaned_data
            login_user = Usuarios.objects.filter(usuario=form_data['user']).values_list()
            
            if login_user:
                return redirect(self.success_url)
            else:
                messages.warning(request, 'Usuario o Contraseña Incorrecta')
                context = {'form': formulario}
                return render(request, self.template_name, context)
        else:
            messages.success(request, 'Usuario o Contraseña Incorrecta')
            context = {'form': formulario}
            return render(request, self.template_name, context)








'''