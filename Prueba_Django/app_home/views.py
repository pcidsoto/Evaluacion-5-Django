from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic import View, ListView
#from .forms import PacientesForm, EditarDatosForm
from app_admin.models import DatosPersonales
import json

'''
class Home(ListView):
    model = DatosPersonales
    form_class = PacientesForm
    template_name = 'app_home/home.html'
    context_object_name = 'pacientes'
    success_url = 'app_home:Home'

    
    def get(self, request, **kwargs):
        pacientes = self.form_class
        #print(DatosPersonales.objects.select_related('id_usuario').all().values_list('id_usuario', 'id_usuario'))
        context = {'pacientes':pacientes}
        return render(request, self.template_name, context)  


    def post(self, request):
        run = request.POST['id_usuario'] 
        datos_paciente = DatosPersonales.objects.filter(id_usuario=run).values()[0]
        pacientes = self.form_class
        context = {'pacientes':pacientes, 
            'datos_paciente': datos_paciente,
            'id':datos_paciente['id']
            }
        return render(request, 'app_home/home.html', context)


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