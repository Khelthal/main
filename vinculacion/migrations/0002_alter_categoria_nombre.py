# Generated by Django 4.0.4 on 2022-06-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinculacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]
