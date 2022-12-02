from django.test import TestCase
from usuarios.models import User, TipoUsuario
from investigadores.models import Investigador, NivelInvestigador


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
