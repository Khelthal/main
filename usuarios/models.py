from django.db import models
from django.contrib.auth.models import AbstractUser

class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo

class User(AbstractUser):
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.DO_NOTHING, null=True, blank=True)
