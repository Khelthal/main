from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

@given(u'que ingreso al sistema en el dominio "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    context.driver.maximize_window()

@given(u'inicio sesión con el usuario "{usuario}" y contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)
    context.driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/form/button").click()

@given(u'hago clic en el tipo "{tipo}"')
def step_impl(context, tipo):
    if tipo == "Investigador":
        context.driver.find_element(By.ID, 'investigador').click()
    if tipo == "Empresa":
        context.driver.find_element(By.ID, 'empresa').click()
    if tipo == "Institución Educativa":
        context.driver.find_element(By.ID, 'institucion-educativa').click()

@given(u'relleno el campo de "{campo}" con "{valor}" en el formulario')
def step_impl(context, campo, valor):
    campo = campo.replace(" ","_")
    context.driver.find_element(By.NAME, campo).send_keys(valor)


@given(u'elijo "{opcion}" en el campo de "{campo}" en el formulario')
def step_impl(context, opcion, campo):
    selects = context.driver.find_elements(By.CLASS_NAME, "form-select")
    for select in selects:
        if select.get_attribute("name") == campo:
            select = Select(select)
            select.select_by_visible_text(opcion)
            break

@when(u'envío la solicitud presionando el botón de Guardar')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, 600)")
    sleep(5)
    context.driver.find_element(By.CLASS_NAME,"btn-primary").click()
    sleep(3)

@then(u'se me indica que mi solicitud fue enviada')
def step_impl(context):
    titulo = context.driver.find_element(By.CLASS_NAME, "titulo-seccion").text
    tituloEsperado = "Sus datos están en espera de ser aprobados por un administrador"

    assert titulo == tituloEsperado

@then(u'se me pide que rellene el campo de "{campo}"')
def step_impl(context, campo):
    campo = campo.replace(" ","_")
    campoEncontrado = context.driver.find_element(By.NAME, campo)
    assert campoEncontrado == context.driver.switch_to.active_element