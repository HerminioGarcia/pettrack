from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@given(u'cuando presiono el boton el correo de verificación de agregacion')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="MailList"]/div/div/div/div/div/div/div/div[2]').click()
    time.sleep(2)


@then(u'puedo ver la mascota ha sido agregada correctamente')
def step_impl(context):
    time.sleep(5)