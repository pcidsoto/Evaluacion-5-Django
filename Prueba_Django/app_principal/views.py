from django.shortcuts import render, redirect
from django.conf import settings
from .forms import LoginForm
import json

from app_admin.models import Usuarios
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib import messages

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
filename_pacientes = '/data/data_registros.json'
filename_noticias = '/data/data_noticias.json'

def get_noticias(filename, settings):
    with open(str(settings.BASE_DIR)+filename, 'r' ,encoding="utf-8") as file:
        noticias=json.load(file)
    return noticias

def get_usuario(filename, settings, run):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)
    user = {}
    for elemento in pacientes['pacientes']:
        for clave in elemento.keys():
            if clave == run:
                user['run'] = clave
                user['password'] = elemento[clave]['password']
    return user

# Create your views here.
def principal(request):
    login_form = LoginForm()
    if request.method == 'POST':    
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            usuario = get_usuario(filename_pacientes,settings, data['user'])
            if usuario and data['user'] == usuario['run'] and data['password'] == usuario['password']:
                
                return redirect('app_home:Home')
            else:
                noticias = get_noticias(filename_noticias, settings)
                enlaces = [
                    {'logo':'/app_principal/logo-doctoralia.png','enlace':'https://www.doctoralia.cl/'},
                    {'logo':'/app_principal/logo-hospital-digital.png','enlace':'https://www.hospitaldigital.gob.cl/'},
                    {'logo':'/app_principal/logoisapres_azul.png','enlace':'http://www.isapre.cl/home'},
                    {'logo':'/app_principal/logo-SAMU-Metropolitano.png','enlace':'https://samu.cl/'},
                    {'logo':'/app_principal/logo-fonasa.png','enlace':'https://www.fonasa.cl/sites/fonasa/inicio'}
                ]
                context ={'noticias':noticias['noticias'],'enlaces':enlaces, 'login_form':login_form}
                return render(request, 'app_principal/index.html', context)
        else:
            return redirect('app_principal:principal')
    else:

        noticias = get_noticias(filename_noticias, settings)
        enlaces = [
            {'logo':'/app_principal/logo-doctoralia.png','enlace':'https://www.doctoralia.cl/'},
            {'logo':'/app_principal/logo-hospital-digital.png','enlace':'https://www.hospitaldigital.gob.cl/'},
            {'logo':'/app_principal/logoisapres_azul.png','enlace':'http://www.isapre.cl/home'},
            {'logo':'/app_principal/logo-SAMU-Metropolitano.png','enlace':'https://samu.cl/'},
            {'logo':'/app_principal/logo-fonasa.png','enlace':'https://www.fonasa.cl/sites/fonasa/inicio'}
        ]
        context ={'noticias':noticias['noticias'],'enlaces':enlaces, 'login_form':login_form}
        return render(request, 'app_principal/index.html', context)'''