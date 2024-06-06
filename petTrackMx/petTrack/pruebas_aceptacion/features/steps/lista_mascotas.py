from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@when(u'presiono el boton lista de mascotas')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="auth2"]/ul/li[3]/a/span').click()
@then(u'puedo ver la lista de las mascotas')
def step_impl(context):
    time.sleep(3)
