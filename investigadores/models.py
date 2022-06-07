from django.db import models
from vinculacion.models import Categoria
from usuarios.models import Investigador

class Investigacion(models.Model):
    titulo = models.TextField()
    categorias = models.ManyToManyField(Categoria)
    autores = models.ManyToManyField(Investigador)
    contenido = models.TextField()
