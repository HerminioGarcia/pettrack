from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'que ingreso a la url "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)

@given(u'escribo mi usuario incorrecto "{username}" y mi password incorrecta "{password}"')
def step_impl(context, username, password):
    
    context.driver.find_element(By.NAME, 'username').send_keys(username)
    time.sleep(3)
    context.driver.find_element(By.NAME, 'password').send_keys(password)

@given(u'escribo mi usuario "{username}" y mi contraseña "{password}"')
def step_impl(context, username, password):
    
    context.driver.find_element(By.NAME, 'username').send_keys(username)
    
    context.driver.find_element(By.NAME, 'password').send_keys(password)


@when(u'presiono el botón de iniciar')
def step_impl(context):
    
    context.driver.find_element(By.ID, 'inicio').click()
    


@then(u'puedo ver que pude entrar exitosamente a la pagina de "{username}"')
def step_impl(context, username):
    div = context.driver.find_element(By.CLASS_NAME, 'profile-name')
    assert username in div.text, f"El usuario {username} no se encuentra en {div.text}"

@then(u'puedo ver "{mensaje}"')
def step_impl(context, mensaje):
    div = context.driver.find_element(By.ID, 'credenciales invalidas')
    assert mensaje in div.text, f"El usuario {mensaje} no se encuentra en {div.text}"


