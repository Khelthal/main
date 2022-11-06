from django.test import TestCase
from django.core.exceptions import ValidationError
from empresas.models import Empresa
from usuarios.models import User, TipoUsuario


# Create your tests here.
class TestSmoke(TestCase):

    def test_smoke(self):
        self.assertEquals(2+2, 4)

    def setUp(self):
        self.tipo_empresa = TipoUsuario.objects.create(tipo="Empresa")
        self.usuario = User.objects.create(
            password="test",
            username="Pruebita",
            email="asd@asd.com",
            is_active=True,
            tipo_usuario=self.tipo_empresa,
            aprobado=True)

    def test_insertar_empresa_conteno(self):
        Empresa.objects.create(
            encargado=self.usuario,
            nombre_empresa="Oxxo",
            latitud=5,
            longitud=5,
            municipio=1,
            colonia="a",
            calle="a",
            numero_exterior=32,
            acerca_de="a")

        self.assertEquals(Empresa.objects.count(), 1)

    def test_insertar_empresa_nombre(self):
        empresa = Empresa.objects.create(
            encargado=self.usuario,
            nombre_empresa="Oxxo",
            latitud=5,
            longitud=5,
            municipio=1,
            colonia="a",
            calle="a",
            numero_exterior=32,
            acerca_de="a")

        empresa2 = Empresa.objects.get(nombre_empresa='Oxxo')

        self.assertEquals(empresa.nombre_empresa, empresa2.nombre_empresa)

    def test_insertar_empresa_validacion(self):
        empresa = Empresa.objects.create(
            encargado=self.usuario,
            nombre_empresa="Oxxo",
            latitud=5,
            longitud=5,
            municipio=1,
            colonia="a",
            calle="a",
            numero_exterior=32,
            acerca_de="a")

        empresa.nombre_empresa = "A"*500
        with self.assertRaises(ValidationError):
            empresa.full_clean()
