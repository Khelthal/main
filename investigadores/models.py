from django.db import models
from vinculacion.models import Categoria
from usuarios.models import Ubicacion, User

class NivelInvestigador(models.Model):
    nivel = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return "Nivel " + str(self.nivel)

class Investigador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.DO_NOTHING, blank=True, null=True)
    nivel = models.ForeignKey(NivelInvestigador, on_delete=models.DO_NOTHING)
    curp = models.TextField()

class Investigacion(models.Model):
    titulo = models.TextField()
    categorias = models.ManyToManyField(Categoria)
    autores = models.ManyToManyField(Investigador)
    contenido = models.TextField()
