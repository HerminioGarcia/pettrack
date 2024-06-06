from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'presiono el botón de iniciar')
def step_impl(context):
    time.sleep(5)
    
    context.driver.find_element(By.ID, 'inicio').click()
    
@given(u'desplegar el menu usuario')

def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[3]/a/span').click()

@given(u'presiono el boton lista de mascotas')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="auth2"]/ul/li[3]/a/span').click()
    

@given(u'prsiono el boton de editar')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[5]/a[2]').click()



@given(u'editamos el campo edad con este nuevo valor "{edad}"')
def step_impl(context,edad):
    time.sleep(2)
    context.driver.find_element(By.NAME, 'edad').send_keys(edad)


@when(u'presionamos el boton guardar')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div[2]/div/form/div[6]/button').click()


@then(u'puedo ver la modificacion en la tabla')
def step_impl(context):
    time.sleep(10)
