# Generated by Django 4.0.4 on 2022-06-17 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investigadores', '0003_remove_investigador_ubicacion_investigador_latitud_and_more'),
        ('usuarios', '0006_alter_tipousuario_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institucioneducativa',
            name='ubicacion',
        ),
        migrations.RemoveField(
            model_name='institucioneducativa',
            name='user',
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
        migrations.DeleteModel(
            name='InstitucionEducativa',
        ),
        migrations.DeleteModel(
            name='Ubicacion',
        ),
    ]
