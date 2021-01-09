# Create your views here.

import datetime
import random
import csv

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings

# Create your views here.

def examenes(request):
    return render(request, 'app_examenes/examenes.html')

'''
def index(request):

    fecha_hora_actual = str(datetime.datetime.now())
    #lista_aleatoria = [i for i in range(0,random.randint(2,10))]
    lista = [1,2,3,4,5,6,7]
    nombres = ["Boris", "Jean Carlos", "Jesús", 
                "Jonathan", "Rocío", "Daniela", "Francisca",
                "Roberta", "Nabucodonosorcito", "Albert", "Alan",
                "Topo Giggio", "Tía Patricia", "Tía Pucherito",
                "Jonathan", "Rocío", "Daniela", "Francisca",
                "Roberta", "Nabucodonosorcito", "Albert", "Alan",
                "Topo Giggio", "Tía Patricia", "Tía Pucherito",
                "Jonathan", "Rocío", "Daniela", "Francisca",
                "Roberta", "Nabucodonosorcito", "Albert", "Alan",
                "Topo Giggio", "Tía Patricia", "Tía Pucherito",
                "Jonathan", "Rocío", "Daniela", "Francisca",
                "Roberta", "Nabucodonosorcito", "Albert", "Alan",
                "Topo Giggio", "Tía Patricia", "Tía Pucherito"]

    context = {'contenido_dinamico': fecha_hora_actual,
                'contenido_dinamico2':  lista,
                'nombres': nombres}
    
    return render(request, 'app1/index.html', context)


def principal(request):
    return render(request, 'app1/principal.html')

def prueba(request):
    return render(request, 'app1/base.html')
    '''