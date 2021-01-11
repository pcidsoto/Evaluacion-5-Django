from django.shortcuts import render, redirect
from .forms import RegistroPaciente


mi_diccionario = []
# Create your views here.
def registro(request):
    if request.method == 'POST':
        print(request.POST)
        data_post = RegistroPaciente(request.POST)
        if data_post.is_valid():
            data_post = data_post.cleaned_data
            print(data_post)
            mi_diccionario.append(dict(data_post))
            formulario = RegistroPaciente()
            context = {'form': formulario, 'registros': mi_diccionario }
            print("PACIENTE AGREGADO")
            return render(request, 'appAdmin/registro.html', context=context)
        else:
            print('NO ES VALIDO')
            context = {'form': data_post, 'registros': mi_diccionario }
            return render(request, 'appAdmin/registro.html', context)
    else:
        print("ENVIANDO FORMULARIO")
        formulario = RegistroPaciente()
        context = {'form': formulario, 'registros': mi_diccionario }
        return render(request, 'appAdmin/registro.html', context=context)

def eliminar(request, nombre):
    print(nombre)
    for index, elemento in enumerate(mi_diccionario):
        if elemento['nombre'] == nombre:
            print(index)
            mi_diccionario.pop(index)
    
    return redirect('appAdmin:registro')
