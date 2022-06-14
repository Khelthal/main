from django.db import models
from django.contrib.auth.models import AbstractUser

class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo

class User(AbstractUser):
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.DO_NOTHING, null=True, blank=True)

class Ubicacion(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return f"({self.latitud}, {self.longitud})"

class InstitucionEducativa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre_institucion = models.CharField(max_length=80)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.DO_NOTHING, blank=True, null=True)

class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.DO_NOTHING, blank=True, null=True)
    nombre_empresa = models.CharField(max_length=80)
