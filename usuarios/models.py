from django.db import models
from django.contrib.auth.models import User, AbstractUser

class TipoUsuario(models.Model):
    tipo = models.TextField()

class User(AbstractUser):
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.DO_NOTHING, null=True, blank=True)

class InstitucionEducativa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Investigador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
