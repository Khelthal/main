from django.db import models
from django.contrib.auth.models import User, AbstractUser

TIPO = [
    ('1', 'Institucion Educativa'),
    ('2', 'Investigador'),
    ('3', 'Empresa'),
]

class User(AbstractUser):
    tipo_usuario = models.CharField('Tipo de Usuario', max_length=1, choices=TIPO)

class InstitucionEducativa(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuario", related_name='datos', on_delete=models.DO_NOTHING)

class Investigador(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuario", related_name='datos', on_delete=models.DO_NOTHING)

class Empresa(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuario", related_name='datos', on_delete=models.DO_NOTHING)