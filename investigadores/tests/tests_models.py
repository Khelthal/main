from django.test import TestCase
from usuarios.models import User
from investigadores.models import (
    SolicitudTrabajo,
    NivelInvestigador,
    Investigador)
from empresas.models import Empresa


class SmokeTest(TestCase):
    def test_smoke(self):
        self.assertTrue(True)


class TestModelSolicitudTrabajo(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username='testuser', password='12345', email="test@mail.com")
        self.usuario.save()

        self.usuario2 = User.objects.create_user(
            username='testuser2', password='12345', email="test2@mail.com")
        self.usuario2.save()

        empresa = Empresa.objects.create(
            encargado=self.usuario2,
            nombre_empresa="Empresa",
            latitud=0,
            longitud=0,
            codigo_postal="12345",
            municipio=1,
            colonia="Colonia",
            calle="Calle",
            numero_exterior="1",
            acerca_de="Acerca de asdasdasdasdasdasdasd",
        )
        empresa.save()

        nivelinvestigadores = NivelInvestigador.objects.create(
            nivel=1,
            descripcion="Descripcion",
        )
        nivelinvestigadores.save()

        self.investigador = Investigador.objects.create(
            user=self.usuario,
            nivel=nivelinvestigadores,
            curp='JISD770826MSPMTV51',
            latitud=0.0,
            longitud=0.0,
            codigo_postal=99360,
            municipio=1,
            colonia='Alamedas',
            calle='Jomulquillo',
            numero_exterior=22,
            acerca_de='Robamos tesis a domicilio'
        )
        self.investigador.save()

        solicitud = SolicitudTrabajo.objects.create(
            titulo="Titulo",
            usuario_a_vincular=self.investigador,
            usuario_solicitante=self.usuario2,
            estado='P',
            estado_investigador='P',
            estado_empleador='P',
            descripcion='test',
            fecha='2020-01-01',
            fecha_finalizado='2020-01-01',
        )
        solicitud.save()

    def test_solicitud_trabajo(self):
        solicitud = SolicitudTrabajo.objects.get(titulo="Titulo")
        self.assertEqual(solicitud.titulo, "Titulo")

    def test_solicitud_trabajo_usuario_a_vincular(self):
        solicitud = SolicitudTrabajo.objects.get(titulo="Titulo")
        self.assertEqual(solicitud.usuario_a_vincular, self.investigador)

    def test_solicitud_trabajo_usuario_solicitante(self):
        solicitud = SolicitudTrabajo.objects.get(titulo="Titulo")
        self.assertEqual(solicitud.usuario_solicitante, self.usuario2)

    def test_solicitud_trabajo_estado(self):
        solicitud = SolicitudTrabajo.objects.get(titulo="Titulo")
        self.assertEqual(solicitud.estado, 'P')

    def test_solicitud_trabajo_estado_investigador(self):
        solicitud = SolicitudTrabajo.objects.get(titulo="Titulo")
        self.assertEqual(solicitud.estado_investigador, 'P')

    def test_solicitud_trabajo_estado_empleador(self):
        solicitud = SolicitudTrabajo.objects.get(titulo="Titulo")
        self.assertEqual(solicitud.estado_empleador, 'P')

    def test_solicitud_trabajo_descripcion(self):
        solicitud = SolicitudTrabajo.objects.get(titulo="Titulo")
        self.assertEqual(solicitud.descripcion, 'test')

    def test_solicitud_trabajo_str(self):
        solicitud = SolicitudTrabajo.objects.get(titulo="Titulo")
        self.assertEqual(str(solicitud), "Titulo")
