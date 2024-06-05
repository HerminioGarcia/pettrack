from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'que ingreso a la url "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    time.sleep(5)  

@when(u'presiono el botón de Lista Mascotas')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li[4]/a').click()
    time.sleep(5)

@then(u'puedo ver mi mascota "{mascota}"')
def step_impl(context, mascota):
    div = context.driver.find_element(By.CSS_SELECTOR, "*:contains('{mascota}')")
    time.sleep(5)
    assert mascota in div.text, f"La {mascota} no se encuentra en {div.text}"

    