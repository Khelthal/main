from behave import given, when
from selenium import webdriver


@given(u'que ingreso al sistema en el dominio "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(context.get_url(url))
    context.driver.maximize_window()

@when(u'me redirijo a la ruta "{url}"')
def step_impl(context, url):
    context.driver.get(context.get_url(url))
    context.driver.maximize_window()
