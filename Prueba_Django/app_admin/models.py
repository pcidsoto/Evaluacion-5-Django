from django.db import models

# Create your models here.
class Administrador(models.Model):
    usuario = models.CharField(primary_key = True, max_length=30)
    contraseña = models.CharField(max_length=20)


class Usuarios(models.Model):
    usuario = models.CharField(primary_key = True, max_length=30)
    contraseña = models.CharField(max_length=20)


class DatosPersonales(models.Model):
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    telefono = models.CharField(max_length=12, blank=True)


class Hemograma(models.Model):
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha = models.DateField()
    hematocrito = models.DecimalField(max_digits=5, decimal_places=2)
    hemoglobina = models.DecimalField(max_digits=5, decimal_places=2)
    rcto_eritrocitos = models.DecimalField(max_digits=5, decimal_places=2)
    v_c_m = models.DecimalField(max_digits=5, decimal_places=2)
    h_c_m = models.DecimalField(max_digits=5, decimal_places=2)
    c_h_c_m = models.DecimalField(max_digits=5, decimal_places=2)
    r_d_w_c_v = models.DecimalField(max_digits=5, decimal_places=2)
    rcto_plaquetas = models.DecimalField(max_digits=5, decimal_places=2)
    rcto_leucocitos = models.DecimalField(max_digits=5, decimal_places=2)
    serie_roja = models.CharField(max_length=30)
    serie_blanca = models.CharField(max_length=30)
    plaquetas = models.CharField(max_length=30)
    
class PerfilBioquimico(models.Model):
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha =  models.DateField()
    glucosa = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    nitrogeno_ureico = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    urea = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    acido_urico = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    colesterol_total = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    proteinas_totales = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    albumina = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    globulina = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    bilirrubina_total = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    transaminasa_gpt_alt = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    transaminasa_got_ast = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    g_glutamiltransferasa = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    deshidrogenasa_lactica = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    fosfatasas_alcalinas = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    calcio = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    fosforo = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    
    
class PerfilLipidico(models.Model):
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha = models.DateField()
    glicemia = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    hdl_colesterol = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    ldl_colesterol = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    colesterol_total = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    trigliceridos = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    colesterol_total_hdl = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    
    
class PresionArterial(models.Model):
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha = models.DateField()
    presion_diatolica_mañana = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    presion_sistolica_mañana = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    presion_diatolica_tarde = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    presion_sistolica_tarde = models.DecimalField(
        max_digits=5, decimal_places=2, blank = True)
    
    
class Medicamento(models.Model):
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha = models.DateField()
    nombre = models.CharField(max_length=30)
    hora = models.TimeField()
    dosis = models.CharField(max_length=30)
    