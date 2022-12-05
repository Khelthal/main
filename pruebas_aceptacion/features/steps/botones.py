from behave import when
from selenium.webdriver.common.by import By


@when(u'hago clic en "{boton}"')
def step_impl(context, boton):
    context.boton.find_element(By.ID, boton).click()

@when(u'confirmo mi decisión')
def step_impl(context):
    context.driver.find_element(By.NAME, "confirmar").click()