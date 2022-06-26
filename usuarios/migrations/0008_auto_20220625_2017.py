# Generated by Django 4.0.5 on 2022-06-25 20:17

from django.db import migrations

def agregar_tipos_usuario(apps, schema_editor):
    TipoUsuario = apps.get_model('usuarios', 'TipoUsuario')

    for tipo in ["Investigador", "Empresa", "Institucion Educativa"]:
        nuevo_tipo_usuario = TipoUsuario()
        nuevo_tipo_usuario.tipo = tipo
        nuevo_tipo_usuario.save()

class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_remove_institucioneducativa_ubicacion_and_more'),
    ]

    operations = [
        migrations.RunPython(agregar_tipos_usuario)
    ]
