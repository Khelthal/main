from django.test import TestCase
from usuarios.models import User, TipoUsuario
from investigadores.models import Investigador, NivelInvestigador
from empresas.models import Empresa
from instituciones_educativas.models import InstitucionEducativa
from django.test import TestCase
from investigadores.models import (
    Investigador,
    NivelInvestigador,
    SolicitudTrabajo)
from usuarios.models import User, TipoUsuario
from django.urls import reverse
from helpers.usuarios_helpers import crear_usuario, crear_tipo_usuario
from helpers.vinculacion_helpers import crear_noticia, crear_area_conocimiento, crear_categoria
from helpers.investigadores_helpers import crear_nivel_investigador, crear_investigador


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


class TestActualizarCuentaInvestigador(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username='prueba-investigador', password='12345')
        self.usuario.save()
        self.client.login(
            username='prueba-investigador', password='12345')
        crear_nivel_investigador(1, "Nivel 1")

    def test_actualizar_perfil(self):
        response = self.client.get('/perfil')
        self.assertEqual(response.status_code, 200)

    def test_actualizar_perfil_investigador_datos_correctos(self):
        ruta_imagen = '/tmp/noticia.png'
        with open(ruta_imagen, 'rb') as imagen:
            datos = {'curp': 'AUCJ011020HZSGRVA1', 'codigo_postal': '99390', 'municipio': 19,
                     'colonia': 'Alamitos', 'calle': 'Mezquite', 'numero_exterior': '29',
                     'acerca_de': 'Info', 'imagen': imagen}
            self.client.post('/formularios/investigador', datos)
            self.assertEquals(
                Investigador.objects.count(), 1)

    def test_actualizar_perfil_investigador_direccion_invalida(self):
        ruta_imagen = '/tmp/noticia.png'
        with open(ruta_imagen, 'rb') as imagen:
            datos = {'curp': 'AUCJ011020HZSGRVA1', 'codigo_postal': '99393', 'municipio': 15,
                     'colonia': 'Durazno', 'calle': 'Frutas', 'numero_exterior': '229',
                     'acerca_de': 'Info', 'imagen': imagen}
            self.client.post('/formularios/investigador', datos)
            self.assertEquals(
                Investigador.objects.count(), 0)


class TestActualizarCuentaEmpresa(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username='prueba-empresa', password='12345')
        self.usuario.save()
        self.client.login(
            username='prueba-empresa', password='12345')
        area = crear_area_conocimiento("Ingeniería", "Las ingenierías")
        crear_categoria("Software", area, "El software")

    def test_actualizar_perfil_empresa_datos_correctos(self):
        ruta_imagen = '/tmp/noticia.png'
        with open(ruta_imagen, 'rb') as imagen:
            datos = {'nombre_empresa': 'Empresa', 'codigo_postal': '99390', 'municipio': 19,
                     "especialidades": [1], 'colonia': 'Alamitos', 'calle': 'Mezquite',
                     'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': imagen}
            self.client.post('/formularios/empresa', datos)
            self.assertEquals(
                Empresa.objects.count(), 1)

    def test_actualizar_perfil_empresa_direccion_invalida(self):
        ruta_imagen = '/tmp/noticia.png'
        with open(ruta_imagen, 'rb') as imagen:
            datos = {
                'nombre_empresa': 'Empresa',
                'codigo_postal': '99390',
                'municipio': 19,
                "especialidades": [1],
                'colonia': 'Durazno',
                'calle': 'Frutas',
                'numero_exterior': '229',
                'acerca_de': 'Info',
                'imagen': imagen
            }
            self.client.post(
                '/formularios/empresa',
                datos
            )
            self.assertEquals(
                Empresa.objects.count(), 0)


class TestActualizarCuentaInstitucionEducativa(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username='prueba-institucion', password='12345')
        self.usuario.save()
        self.client.login(
            username='prueba-institucion', password='12345')
        area = crear_area_conocimiento("Ingeniería", "Las ingenierías")
        crear_categoria("Software", area, "El software")
        nivel = crear_nivel_investigador(1, "Uno")
        tipo_investigador = crear_tipo_usuario("Investigador")
        usuario_investigador = crear_usuario(
            "usuario-investigador",
            "inv@inv.com",
            "12345678",
            tipo_investigador
        )
        crear_investigador(
            usuario=usuario_investigador,
            nivel=nivel,
            curp="AUCJ011020HZSGRVA1",
            latitud=0,
            longitud=0,
            codigo_postal=99390,
            municipio=20,
            colonia="Alamitos",
            calle="Mezquite",
            numero_exterior=29,
            acerca_de="Soy un investigador"
        )

    def test_actualizar_perfil_institucion_datos_correctos(self):
        ruta_imagen = '/tmp/noticia.png'
        with open(ruta_imagen, 'rb') as imagen:
            datos = {'nombre_institucion': 'Institucion', 'codigo_postal': '99390', 'municipio': 19,
                     "especialidades": [1], 'miembros':[2], 'colonia': 'Alamitos', 'calle': 'Mezquite',
                     'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': imagen}
            respuesta = self.client.post('/formularios/institucion_educativa', datos)
            print(respuesta.content)
            self.assertEquals(
                InstitucionEducativa.objects.count(), 1)

    def test_actualizar_perfil_institucion_direccion_invalida(self):
        ruta_imagen = '/tmp/noticia.png'
        with open(ruta_imagen, 'rb') as imagen:
            datos = {'nombre_institucion': 'Institucion', 'codigo_postal': '99350', 'municipio': 19,
                     "especialidades": [1], 'miembros':[2], 'colonia': 'Durazno', 'calle': 'Frutas',
                     'numero_exterior': '239', 'acerca_de': 'Info', 'imagen': imagen}
            self.client.post('/formularios/institucion_educativa', datos)
            self.assertEquals(
                InstitucionEducativa.objects.count(), 0)


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


class TestConsultarNoticias (TestCase):
    def setUp(self):
        crear_usuario(usuario="root", correo="root@root.com",
                      contra="12345678", superusuario=True, staff=True)
        self.client.login(username='root', password='12345678')
        self.escritor = crear_usuario(
            "escritor", "escritor@escritor.com", "12345678")
        self.noticia = crear_noticia(
            "Noticia", "Contenido", self.escritor, "/noticias/noticia.png")

    def test_consultar_listado_noticias(self):
        respuesta = self.client.get("/noticias")
        self.assertEquals(respuesta.status_code, 200)

    def test_consultar_detalle_noticia(self):
        respuesta = self.client.get(f"/noticias/{self.noticia.pk}")
        self.assertEquals(respuesta.status_code, 200)
