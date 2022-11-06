from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'ingreso el correo "{correo}", el usuario "{usuario}" y contraseña "{contra}"')
def step_impl(context, correo, usuario, contra):
    context.driver.find_element(By.NAME, 'email').send_keys(correo)
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)
    context.driver.find_element(By.NAME, 'repassword').send_keys(contra)


@when(u'hago clic en Crear cuenta')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/form/button").click()


@then(u'puedo ver mi nombre de usuario "{usuario}" en la página principal')
def step_impl(context, usuario):
    mensaje = context.driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/div[2]").text
    print(mensaje)
    assert mensaje == f"{usuario} se registró de manera exitosa"
