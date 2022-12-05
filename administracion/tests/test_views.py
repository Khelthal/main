from django.test import TestCase
from usuarios.models import User, TipoUsuario
from investigadores.models import Investigador, NivelInvestigador
from empresas.models import Empresa
from instituciones_educativas.models import InstitucionEducativa
from helpers.instituciones_educativas_helpers import crear_institucion_educativa
from helpers.usuarios_helpers import crear_usuario, crear_tipo_usuario
from helpers.vinculacion_helpers import crear_area_conocimiento, crear_categoria
from helpers.investigadores_helpers import crear_investigador, crear_nivel_investigador


class TestCrudUsuario(TestCase):
    def setUp(self):
        self.usuario = User.objects.create(
            username='testuser',
            aprobado=True,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            email="test@test.com",
        )
        self.usuario.set_password("12345")
        self.usuario.save()
        self.client.login(username='testuser', password='12345')

    def test_crear_usuario(self):
        usuario = {
            "username": "Elias",
            "password": "testiando",
            "email": "elias@redacted.com",
        }
        self.client.post("/administracion/usuarios/nuevo", usuario)
        self.assertEquals(User.objects.count(), 2)

    def test_editar_usuario(self):
        usuario = {
            "username": "Elias",
            "password": "testiando",
            "email": "elias@redacted.com",
        }
        self.client.post(
            f"/administracion/usuarios/editar/{self.usuario.pk}", usuario)
        self.assertEquals(
            User.objects.get(pk=self.usuario.pk).username, "Elias")

    def test_eliminar_usuario(self):
        self.client.post(
            f"/administracion/usuarios/eliminar/{self.usuario.pk}")
        self.assertEquals(User.objects.count(), 0)


class TestCRUDInvestigador(TestCase):
    def setUp(self):
        self.nivel = NivelInvestigador.objects.create(
            nivel=1,
            descripcion="XD"
        )
        self.usuario = User.objects.create(
            username='testuser',
            aprobado=True,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            email="test@test.com",
        )
        self.usuario2 = User.objects.create(
            username='user_investigador',
            aprobado=True,
            is_staff=True,
            is_superuser=True,
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
            user=self.usuario2,
            nivel=self.nivel,
        )
        self.usuario.set_password("12345")
        self.usuario.save()
        self.client.login(username='testuser', password='12345')

    def test_crear_investigador_direccion_valida(self):
        investigador = {
            "acerca_de": "a",
            "calle": "Esmeralda",
            "codigo_postal": 98613,
            "colonia": "Las Joyas",
            "curp": "BEGE010204HZSLNLA5",
            "municipio": 16,
            "numero_exterior": 35,
            "user": self.usuario.pk,
            "nivel": self.nivel.pk,
        }
        self.client.post(
            "/administracion/investigadores/nuevo", investigador)
        self.assertEquals(Investigador.objects.count(), 2)

    def test_crear_investigador_direccion_invalida(self):
        investigador = {
            "acerca_de": "a",
            "calle": "Esmeralda",
            "codigo_postal": 98613,
            "colonia": "Las Joyas",
            "curp": "BEGE010204HZSLNLA5",
            "municipio": 15,
            "numero_exterior": 35,
            "user": self.usuario.pk,
            "nivel": self.nivel.pk,
        }
        self.client.post(
            "/administracion/investigadores/nuevo", investigador)
        self.assertEquals(Investigador.objects.count(), 1)

    def test_editar_investigador_direccion_valida(self):
        investigador = {
            "acerca_de": "actualizado",
            "calle": "Esmeralda",
            "codigo_postal": 98613,
            "colonia": "Las Joyas",
            "curp": "BEGE010204HZSLNLA5",
            "municipio": 16,
            "numero_exterior": 35,
            "nivel": self.nivel.pk,
        }
        self.client.post(
            f"/administracion/investigadores/editar/{self.investigador.pk}",
            investigador)
        self.assertEquals(
            Investigador.objects.get(pk=self.investigador.pk).acerca_de,
            "actualizado")

    def test_editar_investigador_direccion_invalida(self):
        investigador = {
            "acerca_de": "actualizado",
            "calle": "Esmeralda",
            "codigo_postal": 98613,
            "colonia": "Las Joyas",
            "curp": "BEGE010204HZSLNLA5",
            "municipio": 15,
            "numero_exterior": 35,
            "nivel": self.nivel.pk,
        }
        self.client.post(
            f"/administracion/investigadores/editar/{self.investigador.pk}",
            investigador)
        self.assertEquals(
            Investigador.objects.get(pk=self.investigador.pk).acerca_de,
            "a")

    def test_eliminar_investigador(self):
        self.client.post(
            f"/administracion/investigadores/eliminar/{self.investigador.pk}")
        self.assertEquals(Investigador.objects.count(), 0)


class TestSolicitudEmpres(TestCase):

    def setUp(self):
        self.usuario = User.objects.create(
            username='testuser',
            aprobado=True,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            email="test@test.com",
        )
        self.usuario_empresa = User.objects.create(
            username='user_empresa',
            aprobado=False,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            email="test2@test.com",
            tipo_usuario=TipoUsuario.objects.get(tipo="Empresa")
        )
        self.empresa = Empresa.objects.create(
            acerca_de="a",
            calle="Esmeralda",
            codigo_postal=98613,
            colonia="Las Joyas",
            municipio=16,
            numero_exterior=35,
            latitud=0,
            longitud=0,
            encargado=self.usuario_empresa,
            nombre_empresa="EmpresaPrueba"
        )
        self.usuario.set_password("12345")
        self.usuario.save()
        self.client.login(username='testuser', password='12345')

    def test_aceptar_solicitud_empresa(self):
        self.client.get(
            f"/administracion/aprobar_perfil/{self.usuario_empresa.pk}")

        self.assertTrue(
            User.objects.get(pk=self.usuario_empresa.pk).aprobado)

    def test_rechazar_solicitud_empresa(self):
        self.client.post(
            f"/administracion/empresas/eliminar/{self.empresa.pk}")

        self.assertEquals(
            Empresa.objects.count(), 0)


class TestSolicitudInstitucionEducativa (TestCase):
    def setUp(self):
        self.admin = crear_usuario(
            "root",
            "root@root.com",
            "12345",
            superusuario=True,
            staff=True
        )
        self.tipo_institucion = crear_tipo_usuario("Institucion")
        self.tipo_investigador = crear_tipo_usuario("Investigador")
        self.usuario_institucion = crear_usuario(
            "prueba-institucion", "prueba-institucion@prueba.com", "prueba", self.tipo_institucion)
        self.usuario_investigador = crear_usuario(
            "Investigador", "prueba-investigador@prueba.com", "prueba", self.tipo_investigador)
        self.area_conocimiento = crear_area_conocimiento("Ingeniería", "Sobre ingeniería")
        self.categoria = crear_categoria("Software", self.area_conocimiento, "Sobre software")
        self.nivel_1 = crear_nivel_investigador(1, "Nivel 1")
        self.investigador = crear_investigador(
            usuario=self.usuario_investigador,
            nivel=self.nivel_1,
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
        self.institucion_educativa = crear_institucion_educativa(
            encargado=self.usuario_institucion,
            nombre_institucion="Institución Prueba",
            especialidades=[self.categoria],
            latitud=0,
            longitud=0,
            miembros=[self.investigador],
            codigo_postal=99390,
            municipio=20,
            colonia="Alamitos",
            calle="Mezquite",
            numero_exterior=29,
            acerca_de="Soy una institución"
        )
        self.client.login(username='root', password='12345')

    def test_aprobar_solicitud_institucion_educativa(self):
        self.client.get(
            f"/administracion/aprobar_perfil/{self.usuario_institucion.pk}")

        self.assertTrue(
            User.objects.get(pk=self.usuario_institucion.pk).aprobado)

    def test_rechazar_solicitud_institucion_educativa(self):
        self.client.post(
            f"/administracion/instituciones_educativas/eliminar/{self.institucion_educativa.pk}")

        self.assertEquals(
            InstitucionEducativa.objects.count(), 0)