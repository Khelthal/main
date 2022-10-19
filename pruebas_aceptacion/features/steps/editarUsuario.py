from behave import given, then, when
from selenium.webdriver.common.by import By

@given(u'presiono el botón Editar de la fila del usuario "{usuario}"')
def step_impl(context, usuario):
    tabla = context.driver.find_element(By.XPATH, "/html/body/div/div[2]/section[2]/div/div[2]/div/div[2]/div/table/tbody")
    trs = tabla.find_elements(By.TAG_NAME, "tr")

    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, "td")
        usr = tds[0].text

        if usr == usuario:
            botones = tds[4].find_elements(By.TAG_NAME, "a")
            botones[0].click()
            break

@when(u'busque al usuario "{usuario}"')
def step_impl(context, usuario):
    tabla = context.driver.find_element(By.XPATH, "/html/body/div/div[2]/section[2]/div/div[2]/div/div[2]/div/table/tbody")
    trs = tabla.find_elements(By.TAG_NAME, "tr")

    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, "td")
        usr = tds[0].text

        if usr == usuario:
            botones = tds[4].find_elements(By.TAG_NAME, "a")
            botones[0].click()
            break

@given(u'modifico los valores a nombre: "{usuario}", contraseña: "{contra}" y correo: "{correo}"')
def step_impl(context, usuario, contra, correo):
    context.driver.find_element(By.NAME, 'email').clear()
    context.driver.find_element(By.NAME, 'username').clear()
    context.driver.find_element(By.NAME, 'password').clear()
    context.driver.find_element(By.NAME, 'email').send_keys(correo)
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)

@then(u'puedo ver que el usuario "{usuario}" actualizado en la tabla de usuarios')
def step_impl(context, usuario):
    tabla = context.driver.find_element(By.XPATH, "/html/body/div/div[2]/section[2]/div/div[2]/div/div[2]/div/table/tbody")
    trs = tabla.find_elements(By.TAG_NAME, "tr")
    usuarios = []

    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, "td")
        usuarios.append(tds[0].text)

    assert usuario in usuarios, str(usuarios)