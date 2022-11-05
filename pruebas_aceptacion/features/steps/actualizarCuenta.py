from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given(u'que ingreso al sistema en el dominio "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)

@given(u'inicio sesión con el usuario "{usuario}" y contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)
    context.driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/form/button").click()

@given(u'hago clic en el tipo investigador')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[1]/a').click()

@given(u'relleno el formulario con la CURP: "{curp}", el código postal "{cp}", elijo el municipio "{municipio}", la colonia "{colonia}", la calle "{calle}", el número "{numero}", en acerca de agrego "{acerca_de}" y subo la imagen encontrada en "{imagen}"')
def step_impl(context, curp, cp, municipio, colonia, calle, numero, acerca_de, imagen):
    context.driver.find_element(By.NAME, 'curp').send_keys(curp)
    context.driver.find_element(By.NAME, 'codigo_postal').send_keys(cp)

    context.driver.find_element(By.CLASS_NAME, 'choices').click()
    munis = context.driver.find_elements(By.CLASS_NAME, 'choices__item')
    
    for muni in munis:
        if muni.text == municipio:
            muni.click()
            break

    context.driver.find_element(By.NAME, 'colonia').send_keys(colonia)
    context.driver.find_element(By.NAME, 'calle').send_keys(calle)
    context.driver.find_element(By.NAME, 'numero_exterior').send_keys(numero)
    context.driver.find_element(By.NAME, 'acerca_de').send_keys(acerca_de)
    context.driver.find_element(By.NAME, 'imagen').send_keys(imagen)

@when(u'envío la solicitud presionando el botón de Guardar')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, 500)")
    sleep(5)
    context.driver.find_element(By.CLASS_NAME,"btn-primary").click()

@then(u'se me indica que mi solicitud fue enviada')
def step_impl(context):
    titulo = context.driver.find_element(By.CLASS_NAME, "titulo-seccion").text
    tituloEsperado = "Sus datos están en espera de ser aprobados por un administrador"

    assert titulo == tituloEsperado

@then(u'se me pide que rellene el campo de "{campo}"')
def step_impl(context, campo):
    campo = context.driver.find_element(By.NAME, 'curp')
    assert campo == context.driver.switch_to.active_element