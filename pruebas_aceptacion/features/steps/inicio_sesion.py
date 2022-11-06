from behave import given
from selenium.webdriver.common.by import By


@given(u'inicio sesión con el usuario "{usuario}" y contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)
    context.driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/form/button").click()
