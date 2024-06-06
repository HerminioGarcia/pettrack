from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'que ingreso a la dirección "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    time.sleep(2)


@given(u'presiono el texto Has olvidado tu contraseña?')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/form/div[4]/a').click()
    time.sleep(2)


@given(u'pongo mi correo "{email}"')
def step_impl(context, email):
    context.driver.find_element(By.NAME, 'email').send_keys(email)
    time.sleep(2)


@given(u'presiono el botón Enviar')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/form/button').click()
    time.sleep(2)


@then(u'puedo ver que me enviaron un correo para restablecer mi contraseña')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/p[1]')


@given(u'que me voy al enlace "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    time.sleep(2)
    

@given(u'agrego mi correo "{email}"')
def step_impl(context, email):
    context.driver.find_element(By.NAME, 'loginfmt').send_keys(email)
    context.driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    time.sleep(2)


@given(u'agrego mi contraseña "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.NAME, 'passwd').send_keys(password)
    context.driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="acceptButton"]').click()
    time.sleep(2)


@given(u'abro el correo de recuperación de contraseña')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="MailList"]/div/div/div/div/div/div/div/div[2]').click()
    time.sleep(2)


@given(u'abro el enlace del correo')
def step_impl(context):
    time.sleep(5)


@given(u'escribo la nueva contraseña "{psswd}"')
def step_impl(context, psswd):
    context.driver.find_element(By.NAME, 'new_password1').send_keys(psswd)


@given(u'verifico la nueva contraseña "{psswd}"')
def step_impl(context, psswd):
    context.driver.find_element(By.NAME, 'new_password2').send_keys(psswd)
    time.sleep(2)


@given(u'me voy a la pagína de inicio de sesión')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/a').click()
    time.sleep(2)


@then(u'puedo ver que mi contraseña fue reestablecida correctamente')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/h4')
    time.sleep(2)
    
