from behave import given, then, when
from selenium.webdriver.common.by import By

@given(u'presiono el botón Eliminar de la fila del usuario "{usuario}"')
def step_impl(context, usuario):
    tabla = context.driver.find_element(By.XPATH, "/html/body/div/div[2]/section[2]/div/div[2]/div/div[2]/div/table/tbody")
    trs = tabla.find_elements(By.TAG_NAME, "tr")

    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, "td")
        usr = tds[0].text

        if usr == usuario:
            botones = tds[4].find_elements(By.TAG_NAME, "a")
            botones[1].click()
            break


@when(u'hago clic en Confirmar')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/section/div/div[2]/form/button").click()


@then(u'puedo ver que el usuario "{usuario}" ya no se encuentra en la tabla de usuarios')
def step_impl(context, usuario):
    tabla = context.driver.find_element(By.XPATH, "/html/body/div/div[2]/section[2]/div/div[2]/div/div[2]/div/table/tbody")
    trs = tabla.find_elements(By.TAG_NAME, "tr")
    usuarios = []

    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, "td")
        usuarios.append(tds[0].text)

    assert usuario not in usuarios, str(usuarios)