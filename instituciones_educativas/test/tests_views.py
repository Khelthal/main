from django.test import TestCase
from usuarios.models import User


class TestVIewInstitucionesEducativas(TestCase):
    def test_lista_instituciones_estatus(self):
        usuario = User.objects.create(
            username="prueba",  email="prueba@mail.com")
        usuario.set_password("12345678")
        usuario.save()
        self.client.login(username="prueba", password="12345678")
        respuesta = self.client.get('/instituciones_educativas/')
        self.assertEquals(respuesta.status_code, 200)
