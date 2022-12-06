from behave import given
from selenium.webdriver.common.by import By
from helpers.usuarios_helpers import crear_usuario
from time import sleep
from usuarios.models import User


@given(u'inicio sesión con el usuario "{usuario}" y contraseña "{contra}"')
def step_impl(context, usuario, contra):
    crear_usuario(usuario=usuario, correo="prueba@prueba.com", contra=contra)
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)
    context.driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/form/button").click()


@given(u'inicio mi sesión con el usuario "{usuario}" y contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)
    context.driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/form/button").click()


@given(u'inicio sesión como administrador con el usuario "{usuario}" y contraseña "{contra}"')
def step_impl(context, usuario, contra):
    crear_usuario(usuario=usuario, correo="root@root.com", contra=contra, superusuario=True, staff=True)
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)
    context.driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/form/button").click()