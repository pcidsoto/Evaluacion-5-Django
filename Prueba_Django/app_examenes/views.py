import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.conf import settings
from app_admin.models import Hemograma, PerfilLipidico
from django.views.generic import View
from django.views.generic.edit import CreateView
from .forms import HemogramaForm, PerfilLipidicoForm, PacientesFormSelect

class ExamenesView(View):
    select_form = PacientesFormSelect
    template_name = 'app_examenes/examenes.html'
    succes_url = "app_examenes:examen"

    def get(self, request):
        context = {'seleccionar': self.select_form}
        return render(request, 'app_examenes/examenes.html', context)
       
    def post(self, request):
        run = request.POST['pacientes']
        hemograma = list(Hemograma.objects.select_related('id_usuario').\
            filter(id_usuario=run).values())
        context = {
                "seleccionar":self.select_form,
                "hemograma":hemograma,
                "grafico": self.get_datos_hemograma(run)
                }
        perfil_lipidico = list(PerfilLipidico.objects.select_related('id_usuario').\
            filter(id_usuario=run).values())
        context = {
                "seleccionar":self.select_form,
                "perfil_lipidico":perfil_lipidico,
                "grafico": self.get_datos_perfil_lipidico(run)
                }
        return render(request, 'app_examenes/examenes.html', context)

    def get_datos_hemograma(self, run):
        #Obteniendo los datos historicos de los examenes para los graficos
        hemo = Hemograma.objects.select_related('id_usuario').\
            filter(id_usuario=run).\
                values('fecha','hemoglobina','hematocrito',
                'rcto_eritrocitos','rcto_leucocitos',
                'v_c_m','h_c_m','c_h_c_m','r_d_w_c_v','rcto_plaquetas')
        grafico = {
            'fechas':[ str(dato['fecha']) for dato in hemo],
            'hemoglobina':[ float(dato['hemoglobina']) for dato in hemo],
            'hematocrito':[ float(dato['hematocrito']) for dato in hemo],
            'rcto_eritrocitos':[ float(dato['rcto_eritrocitos']) for dato in hemo],
            'rcto_leucocitos':[ float(dato['rcto_leucocitos']) for dato in hemo],
            'v_c_m':[ float(dato['v_c_m']) for dato in hemo],
            'h_c_m':[ float(dato['h_c_m']) for dato in hemo],
            'c_h_c_m':[ float(dato['c_h_c_m']) for dato in hemo],
            'r_d_w_c_v':[ float(dato['r_d_w_c_v']) for dato in hemo],
            'rcto_plaquetas':[ float(dato['rcto_plaquetas']) for dato in hemo],
        } 
        return grafico
    
    def get_datos_perfil_lipidico(self, run):
        #Obteniendo los datos historicos de los examenes para los graficos
        plip = PerfilLipidico.objects.select_related('id_usuario').\
            filter(id_usuario=run).\
                values('fecha','glicemia','hdl_colesterol',
                'ldl_colesterol','colesterol_total',
                'trigliceridos','colesterol_total_hdl')
        grafico = {
            'fechas':[ str(dato['fecha']) for dato in plip],
            'glicemia':[ float(dato['glicemia']) for dato in plip],
            'hdl_colesterol':[ float(dato['hdl_colesterol']) for dato in plip],
            'ldl_colesterol':[ float(dato['ldl_colesterol']) for dato in plip],
            'colesterol_total':[ float(dato['colesterol_total']) for dato in plip],
            'trigliceridos':[ float(dato['trigliceridos']) for dato in plip],
            'colesterol_total_hdl':[ float(dato['colesterol_total_hdl']) for dato in plip],
        } 
        return grafico


class AgregarHemograma(CreateView):
    model = Hemograma
    form_class = HemogramaForm
    template_name = 'app_examenes/add_hemo.html'
    success_url = reverse_lazy('app_examenes:examen')


class AgregarPerfilLipidico(CreateView):
    model = PerfilLipidico
    form_class = PerfilLipidicoForm
    template_name = 'app_examenes/add_plip.html'
    success_url = reverse_lazy('app_examenes:examen')
    
