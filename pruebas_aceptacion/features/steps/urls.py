from behave import given
from selenium import webdriver


@given(u'que ingreso al sistema en el dominio "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    context.driver.maximize_window()
