from django.test import TestCase
from usuarios.models import User


class TestActualizarCuenta(TestCase):
    def setUp(self):
        usuario = User.objects.create_user(
            username='prueba-vista', password='12345')
        usuario.save()
        self.client.login(username='prueba-vista', password='12345')

    def test_vista_actualizar_perfil(self):
        response = self.client.get('/perfil')
        self.assertEqual(response.status_code, 200)

    def test_vista_actualizar_perfil_investigador(self):
        response = self.client.get('/formularios/investigador')
        self.assertEqual(response.status_code, 200)

    def test_vista_actualizar_perfil_empresa(self):
        response = self.client.get('/formularios/empresa')
        self.assertEqual(response.status_code, 200)

    def test_vista_actualizar_perfil_institucion_educativa(self):
        response = self.client.get('/formularios/institucion_educativa')
        self.assertEqual(response.status_code, 200)

    def test_vista_actualizar_perfil_sin_login(self):
        self.client.logout()
        response = self.client.get('/perfil')
        self.assertEqual(response.status_code, 302)

    def test_vista_actualizar_perfil_investigador_sin_login(self):
        self.client.logout()
        response = self.client.get('/formularios/investigador')
        self.assertEqual(response.status_code, 302)

    def test_vista_actualizar_perfil_empresa_sin_login(self):
        self.client.logout()
        response = self.client.get('/formularios/empresa')
        self.assertEqual(response.status_code, 302)

    def test_vista_actualizar_perfil_institucion_educativa_sin_login(self):
        self.client.logout()
        response = self.client.get('/formularios/institucion_educativa')
        self.assertEqual(response.status_code, 302)
