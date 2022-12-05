# Generated by Django 4.1.3 on 2022-12-05 01:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]