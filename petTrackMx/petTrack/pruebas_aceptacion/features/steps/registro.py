from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'que ingreso al enlace "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    time.sleep(2)

@given(u'presiono el botón Regístrate')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/form/div[5]/a').click()
    time.sleep(2)

@given(u'en la pantalla de registro escribo el nomre de usuario "{usuario}" y el correo "{correo}" y la contraseña "{contrasenia}" y repito la contraseña "{recontrasenia}"')
def step_impl(context, usuario, correo, contrasenia, recontrasenia):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'email').send_keys(correo)
    context.driver.find_element(By.NAME, 'password').send_keys(contrasenia)
    context.driver.find_element(By.NAME, 'repassword').send_keys(recontrasenia)
    time.sleep(2)

@when(u'presiono el botón de Registrarse')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/form/div[5]/button').click()
    time.sleep(2)

@then(u'puedo ver que me envió un coreo de verificación')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div')
    time.sleep(2)   

@given(u'que ingreso a la udirección "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    time.sleep(2)

@given(u'escribo mi correo "{email}" y presiono el otón siguiente')
def step_impl(context, email):
    context.driver.find_element(By.NAME, 'loginfmt').send_keys(email)
    context.driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    time.sleep(2)

@given(u'escribo mi contraseña "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.NAME, 'passwd').send_keys(password)
    time.sleep(2)

@given(u'presiono el botón de Iniciar sesión')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    time.sleep(2)

@given(u'presiono el botón de mantener sesión iniciada')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="acceptButton"]').click()
    time.sleep(2)

@given(u'abro el correo de verificación')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="MailList"]/div/div/div/div/div/div/div/div[2]').click()
    time.sleep(2)

@given(u'presiono el botón de verificación')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="UniqueMessageBody_1"]/div/div/div/p[3]/a').click()
    time.sleep(2)


@then(u'puedo ver el mensaje de que mi correo fue verificado')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div')
    time.sleep(2)