from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'prsiono el boton de agregar Mascota')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="auth2"]/ul/li[2]/a/span').click()


@given(u'llenamos el campo nombre con este valor "{nombre}", especie "{especie}" raza "{raza}" edad "{edad}" Numero de telefono Arduino "{arduino}"')
def step_impl(context,nombre,especie,raza,edad,arduino):
    context.driver.find_element(By.NAME, 'nombre').send_keys(nombre)
    context.driver.find_element(By.NAME, 'especie').send_keys(especie)
    context.driver.find_element(By.NAME, 'raza').send_keys(raza)
    context.driver.find_element(By.NAME, 'edad').send_keys(edad)
    context.driver.find_element(By.NAME, 'numero_telefono').send_keys(arduino)
    time.sleep(3)
@when(u'presionamos el boton registrar')
def step_impl(context):
    
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div[2]/div/form/div[6]/button').click()

@then(u'puedo ver la nueva mascota agregada en la tabla')
def step_impl(context):
    time.sleep(7)
