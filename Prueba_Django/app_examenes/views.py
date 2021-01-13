# Create your views here.

import json
from django.shortcuts import render
from django.conf import settings

# Create your views here.
filename = '/app_examenes/data/data_registros.json'

def get_examenes(filename, settings, run):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)
    datos_examenes = {}
    for elemento in pacientes['pacientes']:
        for clave in elemento.keys():
            if clave == run:
                datos_examenes['run'] = clave
                datos_examenes.update(elemento[clave]['datos_personales'])
                datos_examenes.update(elemento[clave]['examenes'])
    return datos_examenes


def examenes(request):
    rut = "22.345.678-9"
    datos = get_examenes(filename, settings, rut)
    context = {"nombre": datos["nombre"], 
               "apellido": datos["apellido"],
               "hemograma": datos["Hemograma"],
               "perfil_lipidico": datos["perfil_lipidico"],
               "presion_arterial": datos["presion_arterial"],
               "perfil_bioquimico": datos["perfil_bioquimico"]}
    return render(request, 'app_examenes/examenes.html', context)
