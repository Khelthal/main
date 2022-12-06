from django.test import TestCase
from usuarios.models import User, TipoUsuario
from investigadores.models import Investigador, NivelInvestigador
from instituciones_educativas.models import InstitucionEducativa


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
        self.assertEqual(response.status_code, 302)

    def test_vista_historial_trabajos_sin_investigador(self):
        usuario = User.objects.get(username='testuser')
        usuario.delete()
        response = self.client.get('/perfil/trabajos/historial')
        self.assertEqual(response.status_code, 302)


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
        self.assertEqual(response.status_code, 302)

    def test_vista_trabajos_en_curso_sin_investigador(self):
        usuario = User.objects.get(username='testuser')
        usuario.delete()
        response = self.client.get('/perfil/trabajos')
        self.assertEqual(response.status_code, 302)


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


class TestConsultaMapa(TestCase):
    def setUp(self):
        usuario = User.objects.create_user(
            username='testuser', password='12345')
        usuario.save()
        self.client.login(username='testuser', password='12345')

    def test_consultar_mapa_loggeado(self):
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)

    def test_consultar_mapa_no_loggeado(self):
        self.client.logout()
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 302)


class TestEliminarUsuario(TestCase):
    def setUp(self):
        usuario = User.objects.create_user(
            username='testuser', password='12345')
        usuario.save()
        self.client.login(username='testuser', password='12345')

    def test_eliminar_cuenta(self):
        self.client.post('/perfil/eliminar')
        self.assertEqual(User.objects.count(), 0)


class TestInstitucionEducativaMiembros(TestCase):
    def setUp(self):
        pass
        self.nivel = NivelInvestigador.objects.create(
            nivel=1,
            descripcion="XD"
        )
        self.usuario_institucion = User.objects.create(
            username='testuser',
            aprobado=True,
            is_active=True,
            tipo_usuario=TipoUsuario.objects.get(tipo="Institucion Educativa"),
            email="test@test.com",
        )
        self.institucion = InstitucionEducativa.objects.create(
            encargado=self.usuario_institucion,
            acerca_de="a",
            calle="Esmeralda",
            codigo_postal=98613,
            colonia="Las Joyas",
            latitud=0,
            longitud=0,
            municipio=16,
            nombre_institucion="Institucioncita",
            numero_exterior=35
        )
        self.usuario_investigador = User.objects.create(
            username='user_investigador',
            aprobado=True,
            is_active=True,
            email="test2@test.com",
            tipo_usuario=TipoUsuario.objects.get(tipo="Investigador")
        )
        self.investigador = Investigador.objects.create(
            acerca_de="a",
            calle="Esmeralda",
            codigo_postal=98613,
            colonia="Las Joyas",
            curp="BEGE010204HZSLNLA5",
            municipio=16,
            numero_exterior=35,
            latitud=0,
            longitud=0,
            user=self.usuario_investigador,
            nivel=self.nivel,
        )
        self.usuario_institucion.set_password("12345")
        self.usuario_institucion.save()
        self.usuario_investigador.set_password("12345")
        self.usuario_investigador.save()
        self.client.login(username='user_investigador', password='12345')
        self.client.get(
            f"/investigador/solicitud_ingreso/{self.institucion.pk}")
        self.client.login(username='testuser', password='12345')

    def test_listar_solicitud_miembros(self):
        r = self.client.get("/institucion_educativa/solicitud_ingreso")
        self.assertEquals(r.status_code, 200)

    def test_listar_miembros(self):
        r = self.client.get("/institucion_educativa/miembros")
        self.assertEquals(r.status_code, 200)

    def test_aceptar_solicitud_miembro(self):
        self.client.get(
            "/institucion_educativa/solicitud_ingreso/" +
            f"{self.investigador.pk}/1")
        self.assertEquals(
            len(
                InstitucionEducativa.objects.get(
                    pk=self.institucion.pk).miembros.all()),
            1)

    def test_rechazar_solicitud_miembro(self):
        self.client.get(
            "/institucion_educativa/solicitud_ingreso/" +
            f"{self.investigador.pk}/0")
        self.assertEquals(
            len(
                InstitucionEducativa.objects.get(
                    pk=self.institucion.pk).miembros.all()),
            0)

    def test_eliminar_miembro(self):
        self.client.get(
            "/institucion_educativa/solicitud_ingreso/" +
            f"{self.investigador.pk}/1")
        self.client.get(
            "/institucion_educativa/miembros/eliminar/" +
            f"{self.investigador.pk}")
        self.assertEquals(
            len(
                InstitucionEducativa.objects.get(
                    pk=self.institucion.pk).miembros.all()),
            0)
