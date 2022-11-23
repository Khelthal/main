from django.test import TestCase
from django.core.exceptions import ValidationError
from vinculacion.models import AreaConocimiento, Categoria


class TestSmoke(TestCase):
    def test_smoke(self):
        self.assertTrue(True)


class TestAreaConocimiento(TestCase):
    def setUp(self):
        self.area = AreaConocimiento(nombre="Test", descripcion="Test")

    def test_nombre_max_length(self):
        max_length = self.area._meta.get_field("nombre").max_length
        self.assertEquals(max_length, 70)

    def test_descripcion_max_length(self):
        max_length = self.area._meta.get_field("descripcion").max_length
        self.assertEquals(max_length, None)

    def test_nombre_blank(self):
        self.area.nombre = ""
        self.assertRaises(ValidationError, self.area.full_clean)

    def test_descripcion_blank(self):
        self.area.descripcion = ""
        self.assertRaises(ValidationError, self.area.full_clean)

    def test_nombre_null(self):
        self.area.nombre = None
        self.assertRaises(ValidationError, self.area.full_clean)

    def test_descripcion_null(self):
        self.area.descripcion = None
        self.assertRaises(ValidationError, self.area.full_clean)

    def test_nombre_str(self):
        self.area.save()
        self.assertEquals(str(self.area), "Test")


class TestCategoria(TestCase):
    def setUp(self):
        self.area = AreaConocimiento(nombre="Test", descripcion="Test")
        self.area.save()
        self.categoria = Categoria(
            nombre="Test",
            area_conocimiento=self.area,
            descripcion="Test")

    def test_nombre_max_length(self):
        max_length = self.categoria._meta.get_field("nombre").max_length
        self.assertEquals(max_length, 30)

    def test_descripcion_max_length(self):
        max_length = self.categoria._meta.get_field("descripcion").max_length
        self.assertEquals(max_length, None)

    def test_nombre_blank(self):
        self.categoria.nombre = ""
        self.assertRaises(ValidationError, self.categoria.full_clean)

    def test_descripcion_blank(self):
        self.categoria.descripcion = ""
        self.assertRaises(ValidationError, self.categoria.full_clean)

    def test_nombre_null(self):
        self.categoria.nombre = None
        self.assertRaises(ValidationError, self.categoria.full_clean)

    def test_descripcion_null(self):
        self.categoria.descripcion = None
        self.assertRaises(ValidationError, self.categoria.full_clean)

    def test_nombre_str(self):
        self.categoria.save()
        self.assertEquals(str(self.categoria), "Test")

    def test_area_conocimiento_null(self):
        self.categoria.area_conocimiento = None
        self.assertRaises(ValidationError, self.categoria.full_clean)

    def test_area_conocimiento_blank(self):
        self.categoria.area_conocimiento = None
        self.assertRaises(ValidationError, self.categoria.full_clean)
