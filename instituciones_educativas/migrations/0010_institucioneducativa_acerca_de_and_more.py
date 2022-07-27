# Generated by Django 4.0.5 on 2022-07-27 19:41

from django.db import migrations, models
import instituciones_educativas.models


class Migration(migrations.Migration):

    dependencies = [
        ('instituciones_educativas', '0009_solicitudingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucioneducativa',
            name='acerca_de',
            field=models.TextField(default='', max_length=1000, verbose_name='Acerca de'),
        ),
        migrations.AddField(
            model_name='institucioneducativa',
            name='imagen',
            field=models.ImageField(default=None, upload_to=instituciones_educativas.models.rutaImagenInstitucion, verbose_name='Imagen de perfil'),
        ),
    ]