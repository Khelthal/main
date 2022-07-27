from django.db import models
from investigadores.models import Investigador
from usuarios.models import User, MUNICIPIOS
from vinculacion.models import Categoria
from administracion.validators import cp_validator

def rutaImagenInstitucion(instance):
    return 'usuarios/instituciones_educativas/institucion_educativa_{0}'.format(instance.encargado.pk)

# Create your models here.
class InstitucionEducativa(models.Model):
    encargado = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre_institucion = models.CharField(max_length=80)
    especialidades = models.ManyToManyField(Categoria)
    latitud = models.FloatField()
    longitud = models.FloatField()
    miembros = models.ManyToManyField(Investigador)
    codigo_postal = models.CharField(max_length=5, validators=[cp_validator])
    municipio = models.IntegerField(choices=MUNICIPIOS)
    colonia = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    numero_exterior = models.PositiveIntegerField()
    acerca_de = models.TextField(verbose_name="Acerca de", max_length=1000, default="")
    imagen = models.ImageField(upload_to=rutaImagenInstitucion, verbose_name="Imagen de perfil", default=None)
    
    def __str__(self):
        return self.nombre_institucion

class SolicitudIngreso(models.Model):
    investigador = models.ForeignKey(Investigador, on_delete=models.CASCADE)
    institucion_educativa = models.ForeignKey(InstitucionEducativa, on_delete=models.CASCADE)