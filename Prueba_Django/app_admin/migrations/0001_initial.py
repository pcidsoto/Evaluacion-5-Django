# Generated by Django 3.1.5 on 2021-01-27 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('usuario', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('contraseña', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('usuario', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('contraseña', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PresionArterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('presion_diatolica_mañana', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('presion_sistolica_mañana', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('presion_diatolica_tarde', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('presion_sistolica_tarde', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilLipidico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('glicemia', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('hdl_colesterol', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('ldl_colesterol', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('colesterol_total', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('trigliceridos', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('colesterol_total_hdl', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilBioquimico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('glucosa', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('nitrogeno_ureico', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('urea', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('acido_urico', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('colesterol_total', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('proteinas_totales', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('albumina', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('globulina', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('bilirrubina_total', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('transaminasa_gpt_alt', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('transaminasa_got_ast', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('g_glutamiltransferasa', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('deshidrogenasa_lactica', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('fosfatasas_alcalinas', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('calcio', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('fosforo', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('nombre', models.CharField(max_length=30)),
                ('hora', models.TimeField()),
                ('dosis', models.CharField(max_length=30)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Hemograma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hematocrito', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hemoglobina', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rcto_eritrocitos', models.DecimalField(decimal_places=2, max_digits=5)),
                ('v_c_m', models.DecimalField(decimal_places=2, max_digits=5)),
                ('h_c_m', models.DecimalField(decimal_places=2, max_digits=5)),
                ('c_h_c_m', models.DecimalField(decimal_places=2, max_digits=5)),
                ('r_d_w_c_v', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rcto_plaquetas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rcto_leucocitos', models.DecimalField(decimal_places=2, max_digits=5)),
                ('serie_roja', models.CharField(max_length=30)),
                ('serie_blanca', models.CharField(max_length=30)),
                ('plaquetas', models.CharField(max_length=30)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='DatosPersonales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido_paterno', models.CharField(max_length=30)),
                ('apellido_materno', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=12)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.usuarios')),
            ],
        ),
    ]