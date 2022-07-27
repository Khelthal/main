# Generated by Django 4.0.5 on 2022-07-27 19:30

from django.db import migrations, models
import empresas.models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0007_alter_empresa_municipio'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='acerca_de',
            field=models.TextField(default='', max_length=500, verbose_name='Acerca de'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen',
            field=models.ImageField(default=None, upload_to=empresas.models.rutaImagenEmpresa, verbose_name='Imagen de perfil'),
        ),
    ]
