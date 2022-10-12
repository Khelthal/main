from pathlib import Path
from distro import version_parts
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

def rutaImagenInvestigador(instance, filename):
    extension = Path(filename).suffix
    return 'usuarios/investigadores/investigador_{0}{1}'.format(instance.user.pk, extension)

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
    acerca_de = models.TextField(verbose_name="Acerca de", max_length=1000, default="")
    imagen = models.ImageField(upload_to=rutaImagenInvestigador, verbose_name="Imagen de perfil", default=None)

    def __str__(self):
        return self.user.username

class Investigacion(models.Model):
    titulo = models.CharField(max_length=500)
    categorias = models.ManyToManyField(Categoria)
    autores = models.ManyToManyField(Investigador)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo

class GrupoInvestigacion(models.Model):
    administradores = models.ManyToManyField(Investigador, related_name='%(class)s_administradores')
    integrantes = models.ManyToManyField(Investigador, related_name='%(class)s_integrantes')

ESTADOS = [
    ("E", "En espera"),
    ("A", "Aceptada"),
    ("R", "Rechazada"),
]

class SolicitudTrabajo(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=200)
    descripcion = models.TextField(verbose_name="Descripción", max_length=5000)
    usuario_a_vincular = models.ForeignKey(Investigador, verbose_name="Usuario a vincular", on_delete=models.CASCADE)
    usuario_solicitante = models.ForeignKey(User, verbose_name="Usuario solicitante", on_delete=models.CASCADE)
    estado = models.CharField(choices=ESTADOS, verbose_name="Estado", max_length=1)
    
    def __str__(self):
        return self.titulo