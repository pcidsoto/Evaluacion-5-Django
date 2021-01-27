from django.shortcuts import render
from .forms import Pacientes
from django.conf import settings
import json
from ..app_admin.models import DatosPersonales
from .forms import DatosPersonalesForm
from django.views.generic import ListView
from django.urls import reverse_lazy

class Home(ListView):
    model = DatosPersonales
    form_class = DatosPersonalesForm
    template_name = 'app_home/plantilla_prueba.html'
    context_object_name = 'datos_personales'
    success_url = reverse_lazy('app_home:prueba')


















filename = '/data/data_registros.json'

def get_paciente(filename, run ,settings):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)

    datos = {}
    for elemento in pacientes['pacientes']:
        for clave in elemento.keys(): 
            if clave == run:
                datos['run'] = clave
                datos.update(elemento[clave]['datos_personales'])
                datos.update(elemento[clave]['datos_contacto'])
                
    return datos


# Create your views here.
def home(request):
    if request.POST: 
        run = request.POST['pacientes'] 
        datos_paciente = get_paciente(filename, run, settings)
        print(datos_paciente)
        pacientes = Pacientes(auto_id=False)
        context = {'pacientes':pacientes, 'datos': datos_paciente}
        return render(request, 'app_home/home.html', context)

    else:
        pacientes = Pacientes(auto_id=False)
        context = {'pacientes':pacientes }
        return render(request, 'app_home/home.html', context)

