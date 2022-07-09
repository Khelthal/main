from django.db import models
from usuarios.models import User
from vinculacion.models import Categoria

# Create your models here.
class Empresa(models.Model):
    encargado = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre_empresa = models.CharField(max_length=80)
    especialidades = models.ManyToManyField(Categoria)
    latitud = models.FloatField()
    longitud = models.FloatField()
    
    def __str__(self):
        return self.nombre_empresa
