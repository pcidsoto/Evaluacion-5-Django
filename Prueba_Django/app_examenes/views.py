import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.conf import settings
from app_admin.models import Hemograma, PresionArterial, PerfilBioquimico, PerfilLipidico
from django.views.generic import View
from django.views.generic.edit import CreateView
#from .forms import HemogramaForm, PresionArterialForm, PerfilBioquimicoForm
#from .forms import PerfilLipidicoForm 
#from .forms import PacientesFormSelect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def usuario_permitido(usuario):
        if usuario.datospersonales.rol == 1:
            validacion = True
        else:
            validacion = False
        return validacion 

class ExamenesView(LoginRequiredMixin,UserPassesTestMixin,View):
    template_name = 'app_examenes/examenes.html'
    succes_url = "app_examenes:examen"

    def test_func(self):
        return usuario_permitido(self.request.user)

    def get(self, request):
        print(self.request.user.id)
        hemograma = list(Hemograma.objects.select_related('id_usuario').\
            filter(usuario_id=self.request.user.id).values())
        
        perfil_lipidico = list(PerfilLipidico.objects.select_related('id_usuario').\
            filter(usuario_id=self.request.user.id).values())
        presionarterial = list(PresionArterial.objects.select_related('id_usuario').\
            filter(usuario_id=self.request.user.id).values())
        perfil_bioquimico = list(PerfilBioquimico.objects.select_related('id_usuario').\
            filter(usuario_id=self.request.user.id).values())
        
        context = {
                "hemograma":hemograma,
                "perfil_lipidico":perfil_lipidico,
                "perfil_bioquimico":perfil_bioquimico,
                "presionarterial":presionarterial,
                "grafico_hemograma": self.get_datos_hemograma(self.request.user.id),
                "grafico_perfil_lipidico": self.get_datos_perfil_lipidico(self.request.user.id),
                "grafico_perfilbioquimico": self.get_datos_perfil_bioquimico(self.request.user.id),
                "grafico_presionarterial": self.get_datos_presionarterial(self.request.user.id),
                }
        
        return render(request, 'app_examenes/examenes.html', context)

    def get_datos_hemograma(self, run):
            #Obteniendo los datos historicos de los examenes para los graficos
        hemo = Hemograma.objects.select_related('id_usuario').\
            filter(usuario_id=run).\
                values('fecha','hemoglobina','hematocrito',
                'rcto_eritrocitos','rcto_leucocitos',
                'v_c_m','h_c_m','c_h_c_m','r_d_w_c_v','rcto_plaquetas')
        grafico_hemograma = {
            'fecha':[ str(dato['fecha']) for dato in hemo],
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
        return grafico_hemograma

    def get_datos_hemograma(self, run):
        #Obteniendo los datos historicos de los examenes para los graficos
        hemo = Hemograma.objects.select_related('id_usuario').\
            filter(usuario_id=run).\
                values('fecha','hemoglobina','hematocrito',
                'rcto_eritrocitos','rcto_leucocitos',
                'v_c_m','h_c_m','c_h_c_m','r_d_w_c_v','rcto_plaquetas')
        grafico_hemograma = {
            'fecha':[ str(dato['fecha']) for dato in hemo],
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
        return grafico_hemograma
    
    def get_datos_perfil_lipidico(self, run):
        #Obteniendo los datos historicos de los examenes para los graficos
        perfil_lipidico = PerfilLipidico.objects.select_related('id_usuario').\
            filter(usuario_id=run).\
                values('fecha','glicemia','hdl_colesterol',
                'ldl_colesterol','colesterol_total',
                'trigliceridos','colesterol_total_hdl')
        grafico_perfil_lipidico = {
            'fecha':[ str(dato['fecha']) for dato in perfil_lipidico],
            'glicemia':[ float(dato['glicemia']) for dato in perfil_lipidico],
            'hdl_colesterol':[ float(dato['hdl_colesterol']) for dato in perfil_lipidico],
            'ldl_colesterol':[ float(dato['ldl_colesterol']) for dato in perfil_lipidico],
            'colesterol_total':[ float(dato['colesterol_total']) for dato in perfil_lipidico],
            'trigliceridos':[ float(dato['trigliceridos']) for dato in perfil_lipidico],
            'colesterol_total_hdl':[ float(dato['colesterol_total_hdl']) for dato in perfil_lipidico],
        } 
        return grafico_perfil_lipidico

    def get_datos_perfil_bioquimico(self, run):
        #Obteniendo los datos historicos de los examenes para los graficos
        perfil_bioquimico = PerfilBioquimico.objects.select_related('id_usuario').\
            filter(usuario_id=run).\
                values('fecha','glucosa','nitrogeno_ureico',
                'urea','acido_urico',
                'colesterol_total','proteinas_totales','albumina','globulina',
                'bilirrubina_total', 'transaminasa_gpt_alt', 'transaminasa_got_ast',
                'g_glutamiltransferasa', 'deshidrogenasa_lactica', 'fosfatasas_alcalinas',
                'calcio', 'fosforo')
        grafico_perfil_bioquimico = {
            'fecha':[ str(dato['fecha']) for dato in perfil_bioquimico],
            'glucosa':[ float(dato['glucosa']) for dato in perfil_bioquimico],
            'nitrogeno_ureico':[ float(dato['nitrogeno_ureico']) for dato in perfil_bioquimico],
            'urea':[ float(dato['urea']) for dato in perfil_bioquimico],
            'acido_urico':[ float(dato['acido_urico']) for dato in perfil_bioquimico],
            'colesterol_total':[ float(dato['colesterol_total']) for dato in perfil_bioquimico],
            'proteinas_totales':[ float(dato['proteinas_totales']) for dato in perfil_bioquimico],
            'albumina':[ float(dato['albumina']) for dato in perfil_bioquimico],
            'globulina':[ float(dato['globulina']) for dato in perfil_bioquimico],
            'bilirrubina_total':[ float(dato['bilirrubina_total']) for dato in perfil_bioquimico],
            'transaminasa_gpt_alt':[ float(dato['transaminasa_gpt_alt']) for dato in perfil_bioquimico],
            'transaminasa_got_ast':[ float(dato['transaminasa_got_ast']) for dato in perfil_bioquimico],
            'g_glutamiltransferasa':[ float(dato['g_glutamiltransferasa']) for dato in perfil_bioquimico],
            'deshidrogenasa_lactica':[ float(dato['deshidrogenasa_lactica']) for dato in perfil_bioquimico],
            'fosfatasas_alcalinas':[ float(dato['fosfatasas_alcalinas']) for dato in perfil_bioquimico],
            'calcio':[ float(dato['calcio']) for dato in perfil_bioquimico],
            'fosforo':[ float(dato['fosforo']) for dato in perfil_bioquimico],
        } 
        return grafico_perfil_bioquimico
    
    def get_datos_presionarterial(self, run):
        #Obteniendo los datos historicos de los examenes para los graficos
        presionarterial = PresionArterial.objects.select_related('id_usuario').\
            filter(usuario_id=run).\
                values('fecha', 'presion_diastolica_mañana', 'presion_sistolica_mañana',
                'presion_diastolica_tarde', 'presion_sistolica_tarde')
        grafico_presionarterial = {
            'fecha':[ str(dato['fecha']) for dato in presionarterial],
            'presion_diastolica_mañana':[ float(dato['presion_diastolica_mañana']) for dato in presionarterial],
            'presion_sistolica_mañana':[ float(dato['presion_sistolica_mañana']) for dato in presionarterial],
            'presion_diastolica_tarde':[ float(dato['presion_diastolica_tarde']) for dato in presionarterial],
            'presion_sistolica_tarde':[ float(dato['presion_sistolica_tarde']) for dato in presionarterial]
        } 
        return grafico_presionarterial


'''
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
    
class AgregarPerfilBioquimico(CreateView):
    model = PerfilBioquimico
    form_class = PerfilBioquimicoForm
    template_name = 'app_examenes/add_perfilbioquimico.html'
    success_url = reverse_lazy('app_examenes:examen')
    

class AgregarPresionArterial(CreateView):
    model = PresionArterial
    form_class = PresionArterialForm
    template_name = 'app_examenes/add_presionarterial.html'
    success_url = reverse_lazy('app_examenes:examen')
'''