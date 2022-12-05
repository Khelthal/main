from behave import then
from selenium.webdriver.common.by import By


@then(u'se muestra el mensaje de éxito "{mensaje}"')
def step_impl(context, mensaje):
    alerta = context.driver.find_element(By.CLASS_NAME, "alert-success")
    assert alerta.text == mensaje 