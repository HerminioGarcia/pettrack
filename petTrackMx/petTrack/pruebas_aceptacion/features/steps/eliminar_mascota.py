from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@when(u'Cuando presiono el boton de eliminar')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.ID, 'eliminar').click()

@when(u'selecciono lista de mascotas')
def step_impl(context):
    context.driver.find_element(By.ID, 'lista').click()
    time.sleep(3)

