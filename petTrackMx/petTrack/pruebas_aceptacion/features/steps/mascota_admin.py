from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'que ingreso url "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@given(u'usuario "{username}" contrasena "{password}"')
def step_impl(context, username, password):

    context.driver.find_element(By.NAME, 'username').send_keys(username)
    time.sleep(3)
    context.driver.find_element(By.NAME, 'password').send_keys(password)


@given(u'presiono el boton de identificarse')
def step_impl(context):

    context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/form/div[3]/input').click()


@given(u'puedo ver mi usuario "{user}"')
def step_impl(context, user):
    div = context.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/strong')
    assert user in div.text, f"El usuario {user} no se encuentra en {div.text}"

    

@when(u'presiono mascotas')
def step_impl(context):

    context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr/th/a').click()

@then(u'puedo ver msj "{mensaje}"')
def step_impl(context, mensaje):
    div = context.driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[1]/h1')
    assert mensaje in div.text, f"El usuario {mensaje} no se encuentra en {div.text}"
