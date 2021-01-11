from django.shortcuts import render, redirect
from .forms import RegistroPaciente
from django.conf import settings
import json

filename = '/appAdmin/static/data/data_registros.json'

def leer_archivo(filename, settings):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)
    return pacientes

def actualizar_archivo(filename, data, settings):
    with open(str(settings.BASE_DIR)+filename, 'w') as file:
        json.dump(data, file)

def leer_pacientes(filename, settings):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)

    lista_pacientes= []
    
    for elemento in pacientes['pacientes']:
        for clave, value in elemento.items(): 
            datos = {}
            datos['run'] = clave
            datos.update(elemento[clave]['datos_personales'])
            datos.update(elemento[clave]['datos_personales'])
            lista_pacientes.append(datos)
    return lista_pacientes

def agregar_paciente(filename, form_data, settings):
    form_data['fecha_nacimiento']=form_data['fecha_nacimiento'].strftime("%Y-%m-%d")

    run = form_data['run']
    datos_personales = {}
    datos_personales['nombre'] = form_data['nombre']
    datos_personales['apellido'] = form_data['apellido']
    datos_personales['edad'] = ''
    datos_personales['f_nacimiento'] = form_data['fecha_nacimiento']

    data ={}
    data[run] = {}
    data[run]['datos_personales'] = datos_personales
    data[run]['datos_contacto'] = {}
    data[run]['examenes'] = {}
    data[run]['examenes']['Hemograma'] = []
    data[run]['examenes']['perfil_lipidico'] = []
    data[run]['examenes']['perfil_bioquimico'] = []
    data[run]['examenes']['presion_arterial'] = []
    data[run]['medicamentos'] = {}
    data[run]['medicamentos']['recetas'] = []
    data[run]['citas'] = {}
    data[run]['citas']['medicos'] = []
    data[run]['citas']['examenes'] = []

    archivo = leer_archivo(filename, settings)
    archivo['pacientes'].append(data)

    actualizar_archivo(filename, archivo, settings)
    

def registro(request):
    if request.method == 'POST':
        data_post = RegistroPaciente(request.POST)
        if data_post.is_valid():
            data_post = data_post.cleaned_data
            agregar_paciente(filename, data_post, settings)
            pacientes = leer_pacientes(filename, settings)
            formulario = RegistroPaciente()
            context = {'form': formulario, 'registros': pacientes }
            print("PACIENTE AGREGADO")
            return render(request, 'appAdmin/registro.html', context=context)
        else:
            print('NO ES VALIDO')
            pacientes = leer_pacientes(filename, settings)
            context = {'form': data_post, 'registros': pacientes }
            return render(request, 'appAdmin/registro.html', context)
    else:
        print("CREANDO FORMULARIO")
        formulario = RegistroPaciente()
        pacientes = leer_pacientes(filename, settings)
        context = {'form': formulario, 'registros': pacientes }
        return render(request, 'appAdmin/registro.html', context=context)


def eliminar(request, run):
    print('ELIMINANDO -> {}'.format(run))
    pacientes = leer_archivo(filename, settings)
    for i, elemento in enumerate(pacientes['pacientes']):
        for clave, valor in elemento.items():
            if clave == run:
                pacientes['pacientes'].pop(i)

    actualizar_archivo(filename, pacientes, settings)
    
    return redirect('appAdmin:registro')
