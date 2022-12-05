from django.db.utils import IntegrityError
from django.test import TestCase
from investigadores.models import (
    Investigador,
    NivelInvestigador,
    SolicitudTrabajo)
from usuarios.models import User, TipoUsuario
from django.core.exceptions import ValidationError


class TestSolicitudTrabajoModel(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestSolicitudTrabajoModel, cls).setUpClass()
        cls.tipo_investigador = TipoUsuario.objects.create(
            tipo="Investigador")
        cls.usuario_investigador = User.objects.create(
            username="Prueba",
            email="asd@asd.com",
            is_active=True,
            tipo_usuario=cls.tipo_investigador,
            aprobado=True)
        cls.usuario_investigador.set_password("test")
        cls.usuario_investigador.save()
        cls.usuario_visitante = User.objects.create(
            username="Visitante",
            email="inv@inv.com",
            is_active=True,
            tipo_usuario=cls.tipo_investigador)
        cls.usuario_visitante.set_password("test")
        cls.usuario_visitante.save()
        cls.nivel_1 = NivelInvestigador.objects.create(
            nivel=1,
            descripcion="lorem"
        )
        cls.investigador = Investigador.objects.create(
            nivel=cls.nivel_1,
            user=cls.usuario_investigador,
            curp="BEGE010204HZSLNLA5",
            latitud=0,
            longitud=0,
            codigo_postal="98613",
            municipio=0,
            colonia="Las joyas",
            calle="Esmeralda",
            numero_exterior=35,
            acerca_de="lorem"
        )

    def test_valido(self):
        SolicitudTrabajo.objects.create(
            descripcion="Solicitud de ejemplo",
            titulo="Solicitud",
            usuario_a_vincular=self.investigador,
            usuario_solicitante=self.usuario_visitante,
            estado="E",
        )

        self.assertEquals(SolicitudTrabajo.objects.count(), 1)

    def test_valido_str(self):
        SolicitudTrabajo.objects.create(
            descripcion="Solicitud de ejemplo",
            titulo="Solicitud",
            usuario_a_vincular=self.investigador,
            usuario_solicitante=self.usuario_visitante,
            estado="E",
        )

        self.assertEquals(
            SolicitudTrabajo.objects.first().__str__(),
            "Solicitud")

    def test_no_titulo(self):
        solicitud = SolicitudTrabajo.objects.create(
            descripcion="Solicitud de ejemplo",
            usuario_a_vincular=self.investigador,
            usuario_solicitante=self.usuario_visitante,
            estado="E",
        )

        with self.assertRaises(ValidationError):
            solicitud.full_clean()

    def test_no_titulo_error(self):
        solicitud = SolicitudTrabajo.objects.create(
            descripcion="Solicitud de ejemplo",
            usuario_a_vincular=self.investigador,
            usuario_solicitante=self.usuario_visitante,
            estado="E",
        )

        try:
            solicitud.full_clean()
            self.assertTrue(False)
        except ValidationError as err:
            self.assertEquals(
                err.message_dict["titulo"],
                ['Este campo no puede estar en blanco.'],
            )

    def test_titulo_vacio(self):
        solicitud = SolicitudTrabajo.objects.create(
            descripcion="Solicitud de ejemplo",
            titulo="",
            usuario_a_vincular=self.investigador,
            usuario_solicitante=self.usuario_visitante,
            estado="E",
        )

        with self.assertRaises(ValidationError):
            solicitud.full_clean()

    def test_titulo_largo(self):
        with self.assertRaises(Exception):
            solicitud = SolicitudTrabajo.objects.create(
                descripcion="Solicitud de ejemplo",
                titulo="a"*201,
                usuario_a_vincular=self.investigador,
                usuario_solicitante=self.usuario_visitante,
                estado="E",
            )

            with self.assertRaises(ValidationError):
                solicitud.full_clean()

    def test_no_descripcion(self):
        solicitud = SolicitudTrabajo.objects.create(
            titulo="Solicitud",
            usuario_a_vincular=self.investigador,
            usuario_solicitante=self.usuario_visitante,
            estado="E",
        )

        with self.assertRaises(ValidationError):
            solicitud.full_clean()

    def test_no_descripcion_error(self):
        solicitud = SolicitudTrabajo.objects.create(
            titulo="Solicitud",
            usuario_a_vincular=self.investigador,
            usuario_solicitante=self.usuario_visitante,
            estado="E",
        )

        try:
            solicitud.full_clean()
            self.assertTrue(False)
        except ValidationError as err:
            self.assertEquals(
                err.message_dict["descripcion"],
                ['Este campo no puede estar en blanco.'],
            )

    def test_descripcion_vacio(self):
        solicitud = SolicitudTrabajo.objects.create(
            descripcion="",
            titulo="Solicitud",
            usuario_a_vincular=self.investigador,
            usuario_solicitante=self.usuario_visitante,
            estado="E",
        )

        with self.assertRaises(ValidationError):
            solicitud.full_clean()

    def test_no_estado(self):
        solicitud = SolicitudTrabajo.objects.create(
            descripcion="",
            titulo="Solicitud",
            usuario_a_vincular=self.investigador,
            usuario_solicitante=self.usuario_visitante,
        )

        with self.assertRaises(ValidationError):
            solicitud.full_clean()

    def test_estado_invalido(self):
        solicitud = SolicitudTrabajo.objects.create(
            descripcion="",
            titulo="Solicitud",
            usuario_a_vincular=self.investigador,
            usuario_solicitante=self.usuario_visitante,
            estado="X",
        )

        with self.assertRaises(ValidationError):
            solicitud.full_clean()

    def test_no_usuario_solicitante(self):
        with self.assertRaises(IntegrityError):
            SolicitudTrabajo.objects.create(
                descripcion="Asd",
                titulo="Solicitud",
                usuario_a_vincular=self.investigador,
                estado="E",
            )

    def test_no_usuario_a_vincular(self):
        with self.assertRaises(IntegrityError):
            SolicitudTrabajo.objects.create(
                descripcion="aaa",
                titulo="Solicitud",
                usuario_solicitante=self.usuario_visitante,
                estado="E",
            )
