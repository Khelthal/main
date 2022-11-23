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
class TestSmoke(TestCase):
    def test_smoke(self):
        self.assertTrue(True)


class TestVistaHistorialTrabajos(TestCase):
    def setUp(self):
        usuario = User.objects.create_user(
            username='testuser', password='12345')
        usuario.save()
        self.client.login(username='testuser', password='12345')

    def test_vista_historial_trabajos(self):
        response = self.client.get('/perfil/trabajos/historial')
        self.assertEqual(response.status_code, 200)

    def test_vista_historial_trabajos_sin_login(self):
        self.client.logout()
        response = self.client.get('/perfil/trabajos/historial')
        self.assertEqual(response.status_code, 404)

    def test_vista_historial_trabajos_sin_investigador(self):
        usuario = User.objects.get(username='testuser')
        usuario.delete()
        response = self.client.get('/perfil/trabajos/historial')
        self.assertEqual(response.status_code, 404)


class TestVistaTrabajosEnCurso(TestCase):
    def setUp(self):
        usuario = User.objects.create_user(
            username='testuser', password='12345')
        usuario.save()
        self.client.login(username='testuser', password='12345')

    def test_vista_trabajos_en_curso(self):
        response = self.client.get('/perfil/trabajos')
        self.assertEqual(response.status_code, 200)

    def test_vista_trabajos_en_curso_sin_login(self):
        self.client.logout()
        response = self.client.get('/perfil/trabajos')
        self.assertEqual(response.status_code, 404)

    def test_vista_trabajos_en_curso_sin_investigador(self):
        usuario = User.objects.get(username='testuser')
        usuario.delete()
        response = self.client.get('/perfil/trabajos')
        self.assertEqual(response.status_code, 404)


class TestVistaRechazarSolicitud(TestCase):
    def setUp(self):
        usuario = User.objects.create_user(
            username='testuser', password='12345')
        usuario.save()
        self.client.login(username='testuser', passworaceptard='12345')

    def test_vista_rechazar_solicitud_sin_login(self):
        self.client.logout()
        response = self.client.get('/perfil/trabajos/rechazar/1')
        self.assertEqual(response.status_code, 404)

    def test_vista_rechazar_solicitud_sin_investigador(self):
        usuario = User.objects.get(username='testuser')
        usuario.delete()
        response = self.client.get('/perfil/trabajos/rechazar/1')
        self.assertEqual(response.status_code, 404)


class TestVistaAceptarSolicitud(TestCase):
    def setUp(self):
        usuario = User.objects.create_user(
            username='testuser', password='12345')
        usuario.save()
        self.client.login(username='testuser', password='12345')

    def test_vista_aceptar_solicitud_sin_login(self):
        self.client.logout()
        response = self.client.get('/perfil/trabajos/aprobar/1')
        self.assertEqual(response.status_code, 404)

    def test_vista_aceptar_solicitud_sin_investigador(self):
        usuario = User.objects.get(username='testuser')
        usuario.delete()
        response = self.client.get('/perfil/trabajos/aprobar/1')
        self.assertEqual(response.status_code, 404)


class TestSolicitarTrabajoNuevo(TestCase):
    def setUp(self):
        usuario = User.objects.create_user(
            username='testuser', password='12345')
        usuario.save()
        self.client.login(username='testuser', password='12345')

    def test_solicitar_trabajo_nuevo_sin_login(self):
        self.client.logout()
        response = self.client.get('/formularios/solicitudTrabajo/')
        self.assertEqual(response.status_code, 404)

    def test_solicitar_trabajo_nuevo_sin_investigador(self):
        usuario = User.objects.get(username='testuser')
        usuario.delete()
        response = self.client.get('/formularios/solicitudTrabajo/')
        self.assertEqual(response.status_code, 404)

