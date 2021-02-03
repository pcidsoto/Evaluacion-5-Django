from django.shortcuts import render
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import View
from app_admin.models import Medicamento
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def usuario_permitido(usuario):
        if usuario.datospersonales.rol == 1:
            validacion = True
        else:
            validacion = False
        return validacion 

class MedicamentoView(LoginRequiredMixin,UserPassesTestMixin,View):
    template_name = 'app_medicamentos/medicamento.html'
    success_url = 'app_medicamentos:medicamento'

    def test_func(self):
        return usuario_permitido(self.request.user)

    def get(self, request):
        datos_paciente = Medicamento.objects.filter(usuario_id = self.request.user.id).values()
        context = {
            'datos':datos_paciente
        }
        return render(request, self.template_name, context)
    
    



 
