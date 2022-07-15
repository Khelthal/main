from tabnanny import verbose
from django.db import models
from vinculacion.models import Categoria
from usuarios.models import User, MUNICIPIOS
from investigadores.validators import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields
from administracion.validators import cp_validator

class NivelInvestigador(models.Model):
    nivel = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return "Nivel " + str(self.nivel)

class Investigador(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE, primary_key=True)
    nivel = models.ForeignKey(NivelInvestigador, on_delete=models.DO_NOTHING)
    curp = models.CharField(max_length=18, validators=[curp_validador])
    latitud = models.FloatField()
    longitud = models.FloatField()
    codigo_postal = models.CharField(max_length=5, validators=[cp_validator])
    municipio = models.IntegerField(choices=MUNICIPIOS)
    colonia = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    numero_exterior = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username

class Investigacion(models.Model):
    titulo = models.CharField(max_length=100)
    categorias = models.ManyToManyField(Categoria)
    autores = models.ManyToManyField(Investigador)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo

class GrupoInvestigacion(models.Model):
    administradores = models.ManyToManyField(Investigador, related_name='%(class)s_administradores')
    integrantes = models.ManyToManyField(Investigador, related_name='%(class)s_integrantes')

ESTADOS = [
    ("P", "En proceso"),
    ("F", "Finalizada"),
    ("I", "Incumplida"),
    ("R", "Rechazada"),
    ("C", "Cancelada"),
]

class SolicitudTrabajo(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=200)
    usuario_a_vincular = models.ForeignKey(Investigador, verbose_name="Usuario a vincular", on_delete=models.DO_NOTHING)
    usuario_solicitante = models.ForeignKey(User, verbose_name="Usuario solicitante", on_delete=models.DO_NOTHING)
    estado = models.CharField(choices=ESTADOS, verbose_name="Estado", max_length=2)