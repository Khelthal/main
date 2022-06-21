# Generated by Django 4.0.4 on 2022-06-18 21:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigadores', '0003_remove_investigador_ubicacion_investigador_latitud_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigador',
            name='curp',
            field=models.CharField(max_length=18, validators=[django.core.validators.RegexValidator(code='curp_invalido', message='El CURP no tiene un formato válido', regex='^([A-Z][AEIOUX][A-Z]{2}\\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\\d])(\\d)$')]),
        ),
    ]