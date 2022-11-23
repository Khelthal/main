from django.test import TestCase
from investigadores.models import (
    Investigador,
    NivelInvestigador,
    SolicitudTrabajo)
from usuarios.models import User, TipoUsuario
from django.urls import reverse


class TestCrearSolicitud(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestCrearSolicitud, cls).setUpClass()
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

    def test_datos_completos(self):
        self.client.login(username="Visitante", password="test")
        self.client.post(
            reverse(
                "vinculacion:solicitud_trabajo_nueva",
                kwargs={
                    "investigador_id": self.investigador.pk
                }
            ),
            {
                "descripcion": "test",
                "titulo": "test"
            }
        )

        self.assertEquals(len(SolicitudTrabajo.objects.all()), 1)

    def test_datos_titulo_vacio(self):
        self.client.login(username="Visitante", password="test")
        try:
            self.client.post(
                reverse(
                    "vinculacion:solicitud_trabajo_nueva",
                    kwargs={
                        "investigador_id": self.investigador.pk
                    }
                ),
                {
                    "descripcion": "test",
                    "titulo": ""
                }
            )
        except Exception:
            pass

        self.assertEquals(len(SolicitudTrabajo.objects.all()), 0)

    def test_datos_titulo_largo(self):
        self.client.login(username="Visitante", password="test")
        try:
            self.client.post(
                reverse(
                    "vinculacion:solicitud_trabajo_nueva",
                    kwargs={
                        "investigador_id": self.investigador.pk
                    }
                ),
                {
                    "descripcion": "test",
                    "titulo": "a"*201
                }
            )
        except Exception:
            pass

        self.assertEquals(SolicitudTrabajo.objects.all().count(), 0)

    def test_datos_no_titulo(self):
        self.client.login(username="Visitante", password="test")
        try:
            self.client.post(
                reverse(
                    "vinculacion:solicitud_trabajo_nueva",
                    kwargs={
                        "investigador_id": self.investigador.pk
                    }
                ),
                {
                    "descripcion": "test",
                }
            )
        except Exception:
            pass

        self.assertEquals(len(SolicitudTrabajo.objects.all()), 0)

    def test_datos_descripcion_vacio(self):
        self.client.login(username="Visitante", password="test")
        try:
            self.client.post(
                reverse(
                    "vinculacion:solicitud_trabajo_nueva",
                    kwargs={
                        "investigador_id": self.investigador.pk
                    }
                ),
                {
                    "descripcion": "",
                    "titulo": "prueba"
                }
            )
        except Exception:
            pass

        self.assertEquals(len(SolicitudTrabajo.objects.all()), 0)

    def test_datos_descripcion_largo(self):
        self.client.login(username="Visitante", password="test")
        try:
            self.client.post(
                reverse(
                    "vinculacion:solicitud_trabajo_nueva",
                    kwargs={
                        "investigador_id": self.investigador.pk
                    }
                ),
                {
                    "descripcion": "a"*5001,
                    "titulo": "prueba"
                }
            )
        except Exception:
            pass

        self.assertEquals(len(SolicitudTrabajo.objects.all()), 0)

    def test_datos_no_descripcion(self):
        self.client.login(username="Visitante", password="test")
        try:
            self.client.post(
                reverse(
                    "vinculacion:solicitud_trabajo_nueva",
                    kwargs={
                        "investigador_id": self.investigador.pk
                    }
                ),
                {
                    "titulo": "prueba"
                }
            )
        except Exception:
            pass

        self.assertEquals(len(SolicitudTrabajo.objects.all()), 0)

    def test_datos_completos_mismo_investigador(self):
        self.client.login(username="Prueba", password="test")
        self.client.post(
            reverse(
                "vinculacion:solicitud_trabajo_nueva",
                kwargs={
                    "investigador_id": self.investigador.pk
                }
            ),
            {
                "descripcion": "test",
                "titulo": "test"
            }
        )

        self.assertEquals(len(SolicitudTrabajo.objects.all()), 0)


class TestResponderSolicitud(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestResponderSolicitud, cls).setUpClass()
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
        cls.solicitud = SolicitudTrabajo.objects.create(
            descripcion="Solicitud de ejemplo",
            titulo="Solicitud",
            usuario_a_vincular=cls.investigador,
            usuario_solicitante=cls.usuario_visitante,
            estado="E",
        )

    def test_aceptar_solicitud_id_valido_investigador(self):
        self.client.login(username="Prueba", password="test")
        r = self.client.get(
            reverse(
                "vinculacion:aceptar_solicitud",
                kwargs={"pk": self.solicitud.pk},
            )
        )

        self.assertEquals(r.status_code, 302)

    def test_aceptar_solicitud_id_invalido_investigador(self):
        self.client.login(username="Prueba", password="test")
        r = self.client.get(
            reverse(
                "vinculacion:aceptar_solicitud",
                kwargs={"pk": 5},
            )
        )

        self.assertEquals(r.status_code, 404)

    def test_rechazar_solicitud_id_valido_investigador(self):
        self.client.login(username="Prueba", password="test")
        r = self.client.get(
            reverse(
                "vinculacion:rechazar_solicitud",
                kwargs={"pk": self.solicitud.pk},
            )
        )

        self.assertEquals(r.status_code, 302)

    def test_rechazar_solicitud_id_invalido_investigador(self):
        self.client.login(username="Prueba", password="test")
        r = self.client.get(
            reverse(
                "vinculacion:rechazar_solicitud",
                kwargs={"pk": 5},
            )
        )

        self.assertEquals(r.status_code, 404)

    def test_aceptar_solicitud_id_valido_no_autorizado(self):
        self.client.login(username="Visitante", password="test")
        r = self.client.get(
            reverse(
                "vinculacion:aceptar_solicitud",
                kwargs={"pk": self.solicitud.pk},
            )
        )

        self.assertEquals(r.status_code, 404)

    def test_aceptar_solicitud_id_invalido_no_autorizado(self):
        self.client.login(username="Visitante", password="test")
        r = self.client.get(
            reverse(
                "vinculacion:aceptar_solicitud",
                kwargs={"pk": 5},
            )
        )

        self.assertEquals(r.status_code, 404)

    def test_rechazar_solicitud_id_valido_no_autorizado(self):
        self.client.login(username="Visitante", password="test")
        r = self.client.get(
            reverse(
                "vinculacion:rechazar_solicitud",
                kwargs={"pk": self.solicitud.pk},
            )
        )

        self.assertEquals(r.status_code, 404)

    def test_rechazar_solicitud_id_invalido_no_autorizado(self):
        self.client.login(username="Visitante", password="test")
        r = self.client.get(
            reverse(
                "vinculacion:rechazar_solicitud",
                kwargs={"pk": 5},
            )
        )

        self.assertEquals(r.status_code, 404)
