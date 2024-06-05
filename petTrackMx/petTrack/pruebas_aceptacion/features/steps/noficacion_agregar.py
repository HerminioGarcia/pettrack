from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@given('que el navegador está abierto')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('navego a Gmail e ingreso mi correo electrónico y contraseña y busco "{correo}"')
def step_impl(context, correo):
    context.driver.get("https://mail.google.com")
    username_input = context.driver.find_element_by_name("Email")
    password_input = context.driver.find_element_by_name("Passwd")
    username_input.send_keys("tu_usuario@gmail.com")
    password_input.send_keys("tu_contraseña")
    search_input = context.driver.find_element_by_name("q")
    search_input.send_keys(correo)
    search_input.send_keys(Keys.RETURN)


@then('debería ver el correo electrónico "{correo}"')
def step_impl(context, correo):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='yW']"))
    )
    email_element = context.driver.find_element_by_xpath("//div[@class='yW']")
    assert correo in email_element.text


@given('que el navegador está abierto')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('navego a Gmail e ingreso mi correo electrónico y contraseña incorrectamente y busco "{correo}"')
def step_impl(context, correo):
    context.driver.get("https://mail.google.com")
    username_input = context.driver.find_element_by_name("Email")
    password_input = context.driver.find_element_by_name("Passwd")
    username_input.send_keys("tu_usuario@gmail.com")
    password_input.send_keys("contraseña_incorrecta")
    search_input = context.driver.find_element_by_name("q")
    search_input.send_keys(correo)
    search_input.send_keys(Keys.RETURN)


@then('debería ver un mensaje de error')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='yW']"))
    )
    error_element = context.driver.find_element_by_xpath("//div[@class='yW']")
    assert "Error" in error_element.text
