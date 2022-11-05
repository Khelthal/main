from behave import given, then, when
from selenium.webdriver.common.by import By

@given(u'agrego los valores de nombre: "{usuario}", contraseña: "{contra}" y correo: "{correo}"')
def step_impl(context, correo, usuario, contra):
    context.driver.find_element(By.NAME, 'email').send_keys(correo)
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)


@when(u'hago clic en Guardar')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/section/div/div/div[2]/div/form/div/div/div[4]/button[1]").click()
    

@then(u'puedo ver al usuario "{usuario}" en la lista de usuarios')
def step_impl(context, usuario):
    tabla = context.driver.find_element(By.XPATH, "/html/body/div/div[2]/section[2]/div/div[2]/div/div[2]/div/table/tbody")
    trs = tabla.find_elements(By.TAG_NAME, "tr")
    usuarios = []

    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, "td")
        usuarios.append(tds[0].text)

    assert usuario in usuarios, str(usuarios)