import json
from django.shortcuts import render
from django.conf import settings
from django.views.generic import View
from . forms import PacientesForm
from app_admin.models import Medicamento

class MedicamentoView(View):
    template_name = 'app_medicamentos/medicamento.html'
    form_class = PacientesForm
    success_url = 'app_medicamentos:medicamento'

    def get(self, request):
        pacientes = self.form_class
        context = {'pacientes':pacientes}
        return render (request, self.template_name, context)
    
    def post(self, request):
        run = request.POST['pacientes']
        datos_paciente = Medicamento.objects.filter(id_usuario = run).values()
        print(datos_paciente)
        pacientes = self.form_class
        context = {'pacientes':pacientes, 'datos': datos_paciente}
        return render(request, self.template_name, context)



'''
# Create your views here.
filename = '/data/data_registros.json'

def get_medicamentos(filename, settings, run):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)
    datos_medicamentos = {}
    for elemento in pacientes['pacientes']:
        for clave in elemento.keys():
            if clave == run:
                datos_medicamentos['run'] = clave
                datos_medicamentos.update(elemento[clave]['datos_personales'])
                datos_medicamentos.update(elemento[clave]['medicamentos'])
    
    return datos_medicamentos

def app_medicamentos(request):
    if request.POST:
        run = request.POST['pacientes'] 
        datos_medicamentos = get_medicamentos(filename, settings, run)
                
        seleccionar = Pacientes()
        context = {'seleccionar':seleccionar, 'nombre':datos_medicamentos['nombre'],
                'apellido':datos_medicamentos['apellido'], 'recetas':datos_medicamentos['recetas']
                }
        return render(request, 'app_medicamentos/medicamento.html', context)
    else:
        seleccionar = Pacientes()
        context = {'seleccionar':seleccionar}
        return render(request, 'app_medicamentos/medicamento.html', context)
'''



 
