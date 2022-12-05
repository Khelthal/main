from behave import when, given
from selenium.webdriver.common.by import By
from time import sleep


@given(u'hago clic en "{boton}"')
def step_impl(context, boton):
    sleep(1)
    context.driver.find_element(By.NAME, boton).click()
    sleep(1)

@given(u'hago clic en la opción "{boton}"')
def step_impl(context, boton):
    context.boton.find_element(By.ID, boton).click()

@when(u'hago clic en la opción "{boton}"')
def step_impl(context, boton):
    context.boton.find_element(By.ID, boton).click()

@when(u'confirmo mi decisión')
def step_impl(context):
    context.driver.find_element(By.NAME, "confirmar").click()