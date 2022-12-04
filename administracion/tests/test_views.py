from django.test import TestCase
from usuarios.models import User, TipoUsuario
from investigadores.models import Investigador, NivelInvestigador
from empresas.models import Empresa


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
