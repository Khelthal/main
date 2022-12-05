# Generated by Django 4.0.5 on 2022-07-14 23:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituciones_educativas', '0006_institucioneducativa_miembros'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucioneducativa',
            name='calle',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institucioneducativa',
            name='codigo_postal',
            field=models.CharField(default=11111, max_length=5, validators=[django.core.validators.RegexValidator(
                code='cp_invalido', message='El código postal no tiene un formato válido', regex='\\d{5}')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institucioneducativa',
            name='colonia',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institucioneducativa',
            name='municipio',
            field=models.IntegerField(choices=[], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institucioneducativa',
            name='numero_exterior',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
