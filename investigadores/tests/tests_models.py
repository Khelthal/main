from django.test import TestCase
from django.core.exceptions import ValidationError
from usuarios.models import User
from investigadores.models import (
    SolicitudTrabajo,
    NivelInvestigador,
    Investigador)
from empresas.models import Empresa
from django.utils import timezone


class TestInvestigador(TestCase):
    def setUp(self):
        self.nivel = NivelInvestigador.objects.create(
            nivel=1,
            descripcion="XD"
        )
        self.usuario = User.objects.create_user(
            username='testuser', password='12345', email="test@mail.com")
        self.usuario.save()

    def test_usuario_requerido(self):
        with self.assertRaises(Exception):
            investigador = Investigador.objects.create(
                acerca_de="a",
                calle="Esmeralda",
                codigo_postal=98613,
                colonia="Las Joyas",
                curp="BEGE010204HZSLNLA5",
                municipio=16,
                numero_exterior=35,
                latitud=0,
                longitud=0,
                # user=self.usuario,
                nivel=self.nivel,
            )

            investigador.full_clean()

    def test_curp_requerido(self):
        investigador = Investigador.objects.create(
            acerca_de="a",
            calle="Esmeralda",
            codigo_postal=98613,
            colonia="Las Joyas",
            # curp="BEGE010204HZSLNLA5",
            municipio=16,
            numero_exterior=35,
            latitud=0,
            longitud=0,
            user=self.usuario,
            nivel=self.nivel,
        )

        with self.assertRaises(ValidationError):
            investigador.full_clean()

    def test_curp_formato(self):
        investigador = Investigador.objects.create(
            acerca_de="a",
            calle="Esmeralda",
            codigo_postal=98613,
            colonia="Las Joyas",
            curp="BEGE010204HZSLNLA",
            municipio=16,
            numero_exterior=35,
            latitud=0,
            longitud=0,
            user=self.usuario,
            nivel=self.nivel,
        )

        with self.assertRaises(ValidationError):
            investigador.full_clean()

    def test_calle_requerido(self):
        investigador = Investigador.objects.create(
            acerca_de="a",
            # calle="Esmeralda",
            codigo_postal=98613,
            colonia="Las Joyas",
            curp="BEGE010204HZSLNLA",
            municipio=16,
            numero_exterior=35,
            latitud=0,
            longitud=0,
            user=self.usuario,
            nivel=self.nivel,
        )

        with self.assertRaises(ValidationError):
            investigador.full_clean()

    def test_descripcion_requerida(self):
        investigador = Investigador.objects.create(
            # acerca_de="a",
            calle="Esmeralda",
            codigo_postal=98613,
            colonia="Las Joyas",
            curp="BEGE010204HZSLNLA",
            municipio=16,
            numero_exterior=35,
            latitud=0,
            longitud=0,
            user=self.usuario,
            nivel=self.nivel,
        )

        with self.assertRaises(ValidationError):
            investigador.full_clean()

    def test_codigo_postal_requerido(self):
        investigador = Investigador.objects.create(
            acerca_de="a",
            calle="Esmeralda",
            # codigo_postal=98613,
            colonia="Las Joyas",
            curp="BEGE010204HZSLNLA",
            municipio=16,
            numero_exterior=35,
            latitud=0,
            longitud=0,
            user=self.usuario,
            nivel=self.nivel,
        )

        with self.assertRaises(ValidationError):
            investigador.full_clean()

    def test_codigo_postal_formato(self):
        investigador = Investigador.objects.create(
            acerca_de="a",
            calle="Esmeralda",
            codigo_postal=9861,
            colonia="Las Joyas",
            curp="BEGE010204HZSLNLA",
            municipio=16,
            numero_exterior=35,
            latitud=0,
            longitud=0,
            user=self.usuario,
            nivel=self.nivel,
        )

        with self.assertRaises(ValidationError):
            investigador.full_clean()

    def test_colonia_requerido(self):
        investigador = Investigador.objects.create(
            acerca_de="a",
            calle="Esmeralda",
            codigo_postal=9861,
            # colonia="Las Joyas",
            curp="BEGE010204HZSLNLA",
            municipio=16,
            numero_exterior=35,
            latitud=0,
            longitud=0,
            user=self.usuario,
            nivel=self.nivel,
        )

        with self.assertRaises(ValidationError):
            investigador.full_clean()

    def test_municipio_requerido(self):
        with self.assertRaises(Exception):
            investigador = Investigador.objects.create(
                acerca_de="a",
                calle="Esmeralda",
                codigo_postal=9861,
                colonia="Las Joyas",
                curp="BEGE010204HZSLNLA",
                # municipio=16,
                numero_exterior=35,
                latitud=0,
                longitud=0,
                user=self.usuario,
                nivel=self.nivel,
            )

            investigador.full_clean()

    def test_numero_exterior_requerido(self):
        with self.assertRaises(Exception):
            investigador = Investigador.objects.create(
                acerca_de="a",
                calle="Esmeralda",
                codigo_postal=9861,
                colonia="Las Joyas",
                curp="BEGE010204HZSLNLA",
                municipio=16,
                # numero_exterior=35,
                latitud=0,
                longitud=0,
                user=self.usuario,
                nivel=self.nivel,
            )

            investigador.full_clean()

    def test_nivel_requerido(self):
        with self.assertRaises(Exception):
            investigador = Investigador.objects.create(
                acerca_de="a",
                calle="Esmeralda",
                codigo_postal=9861,
                colonia="Las Joyas",
                curp="BEGE010204HZSLNLA",
                municipio=16,
                numero_exterior=35,
                latitud=0,
                longitud=0,
                user=self.usuario,
                # nivel=self.nivel,
            )

            investigador.full_clean()

    def test_latitud_requerido(self):
        with self.assertRaises(Exception):
            investigador = Investigador.objects.create(
                acerca_de="a",
                calle="Esmeralda",
                codigo_postal=9861,
                colonia="Las Joyas",
                curp="BEGE010204HZSLNLA",
                municipio=16,
                numero_exterior=35,
                # latitud=0,
                longitud=0,
                user=self.usuario,
                nivel=self.nivel,
            )

            investigador.full_clean()

    def test_longitud_requerido(self):
        with self.assertRaises(Exception):
            investigador = Investigador.objects.create(
                acerca_de="a",
                calle="Esmeralda",
                codigo_postal=9861,
                colonia="Las Joyas",
                curp="BEGE010204HZSLNLA",
                municipio=16,
                numero_exterior=35,
                latitud=0,
                # longitud=0,
                user=self.usuario,
                nivel=self.nivel,
            )

            investigador.full_clean()


class TestNivelInvestigador(TestCase):
    def test_nivel_requerido(self):
        with self.assertRaises(Exception):
            NivelInvestigador.objects.create(
                # nivel=1,
                descripcion="XD"
            )

    def test_descripcion_requerida(self):
        nivel = NivelInvestigador.objects.create(
            nivel=1,
            # descripcion="XD"
        )
        with self.assertRaises(ValidationError):
            nivel.full_clean()


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
            fecha=timezone.now(),
            fecha_finalizado=timezone.now(),
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
