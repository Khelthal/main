from django.db import models
from usuarios.models import User

# Create your models here.
class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre_empresa = models.CharField(max_length=80)
    latitud = models.FloatField()
    longitud = models.FloatField()
