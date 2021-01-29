from django.shortcuts import render
from django.conf import settings
from django.views.generic import View
from .forms import Pacientes
from app_admin.models import DatosPersonales
import json


class Home(View):
    template_name = 'app_home/home.html'
    form_class = Pacientes
    success_url = 'app_home:Home'


    def get(self, request):
        pacientes = self.form_class
        #print(DatosPersonales.objects.select_related('id_usuario').all().values_list('id_usuario', 'id_usuario'))
        context = {'pacientes':pacientes }
        return render(request, self.template_name, context)  


    def post(self, request):
        run = request.POST['pacientes'] 
        datos_paciente = DatosPersonales.objects.filter(id_usuario=run).values()[0]
        print(datos_paciente)
        pacientes = self.form_class
        context = {'pacientes':pacientes, 'datos_paciente': datos_paciente}
        return render(request, 'app_home/home.html', context)

#editar pacientes


    def editar_paciente(request, id):
        paciente= DatosPersonales.objects.get(id=id)     


'''filename = '/data/data_registros.json'

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
        return render(request, 'app_home/home.html', context)'''

