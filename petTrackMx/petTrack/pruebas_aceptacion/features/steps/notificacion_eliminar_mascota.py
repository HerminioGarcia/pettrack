from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time





@given(u'que ingreso a la url {url}')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@then(u'puedo ver el correo que llego de la eliminacion correcta')
def step_impl(context):
    time.sleep(5)

@given(u'cuando el boton de eliminar')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[5]/a[1]').click()


@then(u'puedo ver que la mascota ya no esta en la tabla')
def step_impl(context):
    time.sleep(5)


@given(u'cuando presiono el boton el correo de verificación de eliminacion')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="MailList"]/div/div/div/div/div/div/div/div[2]').click()
    time.sleep(2)


@then(u'puedo ver la mascota ha sido eliminada correctamente')
def step_impl(context):
    time.sleep(5)