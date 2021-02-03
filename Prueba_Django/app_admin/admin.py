from django.contrib import admin
from .models import DatosPersonales,Hemograma,PerfilBioquimico,\
    PerfilLipidico,PresionArterial,Medicamento

# Register your models here.
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display=('fecha_nacimiento', 'telefono', 'direccion')


class HemogramaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hemoglobina', 'hematocrito','rcto_eritrocitos',
    'rcto_leucocitos','v_c_m','h_c_m','c_h_c_m','r_d_w_c_v','rcto_plaquetas')


class PerfilBioquimicoAdmin(admin.ModelAdmin):
    list_display  = ('fecha','glucosa','nitrogeno_ureico','urea',
    'acido_urico','colesterol_total','proteinas_totales','albumina',
    'globulina','bilirrubina_total', 'transaminasa_gpt_alt', 
    'transaminasa_got_ast','g_glutamiltransferasa', 
    'deshidrogenasa_lactica', 'fosfatasas_alcalinas','calcio', 'fosforo')


class PerfilLipidicoAdmin(admin.ModelAdmin):
    list_display = ('fecha','glicemia','hdl_colesterol',
                'ldl_colesterol','colesterol_total',
                'trigliceridos','colesterol_total_hdl')


class PresionArterialAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'presion_diastolica_mañana', 'presion_sistolica_mañana', 
    'presion_diastolica_tarde', 'presion_sistolica_tarde')


class MedicamentosAdmin(admin.ModelAdmin):
    list_display =('fecha', 'nombre', 'hora', 'dosis')

admin.site.register(DatosPersonales, DatosPersonalesAdmin)
admin.site.register(Hemograma, HemogramaAdmin)
admin.site.register(PerfilBioquimico, PerfilBioquimicoAdmin)
admin.site.register(PerfilLipidico, PerfilLipidicoAdmin)
admin.site.register(PresionArterial, PresionArterialAdmin)
admin.site.register(Medicamento, MedicamentosAdmin)