from behave import given
from selenium import webdriver
from helpers.usuarios_helpers import crear_tipo_usuario, crear_usuario
from helpers.instituciones_educativas_helpers import crear_institucion_educativa
from helpers.vinculacion_helpers import crear_area_conocimiento, crear_categoria
from helpers.investigadores_helpers import crear_nivel_investigador, crear_investigador
import navegador

@given(u'que existe una solicitud de una institución educativa llamada "{nombre_institucion}"')
def step_impl(context, nombre_institucion):
    context.driver = navegador.get_navegador()
    context.tipo_institucion = crear_tipo_usuario("Institucion")
    context.tipo_investigador = crear_tipo_usuario("Investigador")
    context.usuario_institucion = crear_usuario(
        nombre_institucion, "prueba-institucion@prueba.com", "prueba", context.tipo_institucion)
    context.usuario_investigador = crear_usuario(
        "Investigador", "prueba-investigador@prueba.com", "prueba", context.tipo_investigador)
    context.area_conocimiento = crear_area_conocimiento("Ingeniería", "Sobre ingeniería")
    context.categoria = crear_categoria("Software", context.area_conocimiento, "Sobre software")
    context.nivel_1 = crear_nivel_investigador(1, "Nivel 1")
    context.investigador = crear_investigador(
        usuario=context.usuario_investigador,
        nivel=context.nivel_1,
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
    context.institucion_educativa = crear_institucion_educativa(
        encargado=context.usuario_institucion,
        nombre_institucion="Institución Prueba",
        especialidades=[context.categoria],
        latitud=0,
        longitud=0,
        miembros=[context.investigador],
        codigo_postal=99390,
        municipio=20,
        colonia="Alamitos",
        calle="Mezquite",
        numero_exterior=29,
        acerca_de="Soy una institución"
    )
