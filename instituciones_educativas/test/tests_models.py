from django.test import TestCase
from instituciones_educativas.models import InstitucionEducativa
from usuarios.models import User, TipoUsuario

class TestSmoke(TestCase):

    def test_smoke(self):
        self.assertEquals(2+2,4)

    def test_agregar_institucion_educativa(self):
        tipo_institucion = TipoUsuario.objects.create("Institucion Educativa")
        usuario = User.objects.create(password="test", username="prueba", email="prueba@mail.com", is_active="True", tipo_usuario=tipo_institucion)
        institucion = InstitucionEducativa.objects.create(encargado=usuario, nombre_institucion="UAZ", latitud=5, longitud=5, municipio=1, colonia="a", calle="a", numero_exterior=32, codigo_postal=99393)
        
        institucion2 = InstitucionEducativa.objects.get(nombre_institucion="UAZ")
        self.assertEquals(institucion, institucion2)