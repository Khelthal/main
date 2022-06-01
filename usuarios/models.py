from django.db import models
from django.contrib.auth.models import User, AbstractUser

TIPO_USUARIO = [
    ('0', 'Invitado'), 
    ('1', 'Institucion Educativa'),
    ('2', 'Investigador'),
    ('3', 'Empresa'),
]

class User(AbstractUser):
    tipo_usuario = models.PositiveSmallIntegerField(choices=TIPO_USUARIO)

class InstitucionEducativa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Investigador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)