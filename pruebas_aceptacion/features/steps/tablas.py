from behave import given, then
from selenium.webdriver.common.by import By
from time import sleep

@given(u'busco el registro de "{nombre_registro}" en la tabla de "{nombre_tabla}"')
def step_impl(context, nombre_registro, nombre_tabla):
    nombre_tabla = nombre_tabla.replace(" ", "-")
    tabla = context.driver.find_element(By.NAME, nombre_tabla)
    tbody = tabla.find_element(By.TAG_NAME, "tbody")
    trs = tbody.find_elements(By.TAG_NAME, "tr")

    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, "td")
        registro = tds[0].text

        if registro == nombre_registro:
            context.boton = tds[-1]
            break

@then(u'se muestra el registro de "{nombre_registro}" en la tabla de "{nombre_tabla}"')
def step_impl(context, nombre_registro, nombre_tabla):
    nombre_tabla = nombre_tabla.replace(" ", "-")
    tabla = context.driver.find_element(By.NAME, nombre_tabla)
    tbody = tabla.find_element(By.TAG_NAME, "tbody")
    trs = tbody.find_elements(By.TAG_NAME, "tr")

    registros = []

    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, "td")
        registros.append(tds[0].text)

    assert nombre_registro in registros

@then(u'no se encuentra el registro de "{nombre_registro}" en la tabla de "{nombre_tabla}"')
def step_impl(context, nombre_registro, nombre_tabla):
    nombre_tabla = nombre_tabla.replace(" ", "-")
    tabla = context.driver.find_element(By.NAME, nombre_tabla)
    tbody = tabla.find_element(By.TAG_NAME, "tbody")
    trs = tbody.find_elements(By.TAG_NAME, "tr")

    registros = []

    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, "td")
        registros.append(tds[0].text)

    assert nombre_registro not in registros