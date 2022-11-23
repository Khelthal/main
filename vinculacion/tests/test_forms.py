from django.test import TestCase
from usuarios.models import User
from administracion.forms import FormInvestigadorBase, FormEmpresaUpdate, FormInstitucionEducativaUpdate
from vinculacion.models import Categoria, AreaConocimiento
from investigadores.models import Investigador


class TestActualizarCuentaInvestigador(TestCase):
    def setUp(self):
        usuario = User.objects.create_user(
            username='prueba-form-investigador', password='12345')
        usuario.save()
        self.client.login(
            username='prueba-form-investigador', password='12345')

    def test_investigador_curp_incorrecto(self):
        datos = {'curp': 'incorrecto', 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos',
                 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInvestigadorBase(data=datos)
        self.assertFalse(form.is_valid())

    def test_investigador_codigo_postal_incorrecto(self):
        datos = {'curp': 'incorrecto', 'codigo_postal': '0', 'municipio': 'Jerez', 'colonia': 'Alamitos',
                 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInvestigadorBase(data=datos)
        self.assertFalse(form.is_valid())

    def test_investigador_numero_exterior_incorrecto(self):
        datos = {'curp': 'incorrecto', 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos',
                 'calle': 'Mezquite', 'numero_exterior': '-1', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInvestigadorBase(data=datos)
        self.assertFalse(form.is_valid())

    def test_investigador_imagen_incorrecta(self):
        datos = {'curp': 'incorrecto', 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos',
                 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/incorrecto.txt'}
        form = FormInvestigadorBase(data=datos)
        self.assertFalse(form.is_valid())

    def test_investigador_curp_vacio(self):
        datos = {'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos',
                 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInvestigadorBase(data=datos)
        self.assertFalse(form.is_valid())

    def test_investigador_codigo_postal_vacio(self):
        datos = {'curp': 'AUCJ011020HZSGRVA1', 'municipio': 'Jerez', 'colonia': 'Alamitos',
                 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInvestigadorBase(data=datos)
        self.assertFalse(form.is_valid())

    def test_investigador_municipio_vacio(self):
        datos = {'curp': 'AUCJ011020HZSGRVA1', 'codigo_postal': '99390', 'colonia': 'Alamitos',
                 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInvestigadorBase(data=datos)
        self.assertFalse(form.is_valid())

    def test_investigador_colonia_vacia(self):
        datos = {'curp': 'AUCJ011020HZSGRVA1', 'codigo_postal': '99390', 'municipio': 'Jerez',
                 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInvestigadorBase(data=datos)
        self.assertFalse(form.is_valid())

    def test_investigador_calle_vacia(self):
        datos = {'curp': 'AUCJ011020HZSGRVA1', 'codigo_postal': '99390', 'municipio': 'Jerez',
                 'colonia': 'Alamitos', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInvestigadorBase(data=datos)
        self.assertFalse(form.is_valid())

    def test_investigador_numero_exterior_vacio(self):
        datos = {'curp': 'AUCJ011020HZSGRVA1', 'codigo_postal': '99390', 'municipio': 'Jerez',
                 'colonia': 'Alamitos', 'calle': 'Mezquite', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInvestigadorBase(data=datos)
        self.assertFalse(form.is_valid())

    def test_investigador_acerca_de_vacio(self):
        datos = {'curp': 'AUCJ011020HZSGRVA1', 'codigo_postal': '99390', 'municipio': 'Jerez',
                 'colonia': 'Alamitos', 'calle': 'Mezquite', 'numero_exterior': '29', 'imagen': '/tmp/foto.png'}
        form = FormInvestigadorBase(data=datos)
        self.assertFalse(form.is_valid())

    def test_investigador_imagen_vacia(self):
        datos = {'curp': 'AUCJ011020HZSGRVA1', 'codigo_postal': '99390', 'municipio': 'Jerez',
                 'colonia': 'Alamitos', 'calle': 'Mezquite', 'numero_exterior': '29'}
        form = FormInvestigadorBase(data=datos)
        self.assertFalse(form.is_valid())


class TestActualizarCuentaEmpresa(TestCase):
    def setUp(self):
        usuario = User.objects.create_user(
            username='prueba-form-empresa', password='12345')
        usuario.save()
        self.client.login(username='prueba-form-empresa', password='12345')

        AreaConocimiento.objects.create(nombre='Software', descripcion='Chido')
        area = AreaConocimiento.objects.get(nombre='Software')
        Categoria.objects.create(
            nombre='Cloud', area_conocimiento=area, descripcion='Chido')

    def test_empresa_nombre_empresa_vacia(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'especialidades': [especialidad], 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos',
                 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormEmpresaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_empresa_especialidades_vacias(self):
        datos = {'nombre_empresa': 'Empresa juve', 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos',
                 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormEmpresaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_empresa_codigo_postal_vacio(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'nombre_empresa': 'Empresa juve', 'especialidades': [
            especialidad], 'municipio': 'Jerez', 'colonia': 'Alamitos', 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormEmpresaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_empresa_municipio_vacio(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'nombre_empresa': 'Empresa juve', 'especialidades': [
            especialidad], 'codigo_postal': '99390', 'colonia': 'Alamitos', 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormEmpresaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_empresa_nombre_colonia_vacio(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'nombre_empresa': 'Empresa juve', 'especialidades': [
            especialidad], 'codigo_postal': '99390', 'municipio': 'Jerez', 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormEmpresaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_empresa_nombre_calle_vacia(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'nombre_empresa': 'Empresa juve', 'especialidades': [
            especialidad], 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormEmpresaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_empresa_nombre_numero_exterior_vacio(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'nombre_empresa': 'Empresa juve', 'especialidades': [
            especialidad], 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos', 'calle': 'Mezquite', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormEmpresaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_empresa_nombre_acerca_de_vacio(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'nombre_empresa': 'Empresa juve', 'especialidades': [
            especialidad], 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos', 'calle': 'Mezquite', 'numero_exterior': '29', 'imagen': '/tmp/foto.png'}
        form = FormEmpresaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_empresa_nombre_imagen_vacia(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'nombre_empresa': 'Empresa juve', 'especialidades': [
            especialidad], 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos', 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info'}
        form = FormEmpresaUpdate(data=datos)
        self.assertFalse(form.is_valid())


class TestActualizarCuentaInstitucion(TestCase):
    def setUp(self):
        usuario = User.objects.create_user(
            username='prueba-form-institucion', password='12345')
        usuario.save()
        self.client.login(username='prueba-form-institucion', password='12345')

        AreaConocimiento.objects.create(nombre='Software', descripcion='Chido')
        area = AreaConocimiento.objects.get(nombre='Software')
        Categoria.objects.create(
            nombre='Cloud', area_conocimiento=area, descripcion='Chido')

    def test_institucion_nombre_institucion_vacia(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'especialidades': [especialidad], 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos',
                 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInstitucionEducativaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_institucion_especialidades_vacias(self):
        datos = {'nombre_institucion': 'Institucion juve', 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos',
                 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInstitucionEducativaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_institucion_codigo_postal_vacio(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'nombre_institucion': 'Institucion juve', 'especialidades': [
            especialidad], 'municipio': 'Jerez', 'colonia': 'Alamitos', 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInstitucionEducativaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_institucion_municipio_vacio(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'nombre_institucion': 'Institucion juve', 'especialidades': [
            especialidad], 'codigo_postal': '99390', 'colonia': 'Alamitos', 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInstitucionEducativaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_institucion_nombre_colonia_vacio(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'nombre_institucion': 'Institucion juve', 'especialidades': [
            especialidad], 'codigo_postal': '99390', 'municipio': 'Jerez', 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInstitucionEducativaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_institucion_nombre_calle_vacia(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'nombre_institucion': 'Institucion juve', 'especialidades': [
            especialidad], 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos', 'numero_exterior': '29', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInstitucionEducativaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_institucion_nombre_numero_exterior_vacio(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'nombre_institucion': 'Institucion juve', 'especialidades': [
            especialidad], 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos', 'calle': 'Mezquite', 'acerca_de': 'Info', 'imagen': '/tmp/foto.png'}
        form = FormInstitucionEducativaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_institucion_nombre_acerca_de_vacio(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'nombre_institucion': 'Institucion juve', 'especialidades': [
            especialidad], 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos', 'calle': 'Mezquite', 'numero_exterior': '29', 'imagen': '/tmp/foto.png'}
        form = FormInstitucionEducativaUpdate(data=datos)
        self.assertFalse(form.is_valid())

    def test_institucion_nombre_imagen_vacia(self):
        especialidad = Categoria.objects.get(nombre='Cloud')
        datos = {'nombre_institucion': 'Institucion juve', 'especialidades': [
            especialidad], 'codigo_postal': '99390', 'municipio': 'Jerez', 'colonia': 'Alamitos', 'calle': 'Mezquite', 'numero_exterior': '29', 'acerca_de': 'Info'}
        form = FormInstitucionEducativaUpdate(data=datos)
        self.assertFalse(form.is_valid())
