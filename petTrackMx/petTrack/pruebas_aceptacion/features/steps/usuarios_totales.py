from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('el administrador ha iniciado sesión en el panel de administración')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:8000/admin")
    username_input = context.driver.find_element_by_name("username")
    password_input = context.driver.find_element_by_name("password")
    username_input.send_keys("tu_usuario")
    password_input.send_keys("tu_contraseña")
    context.driver.find_element_by_name("login").click()

@when('el administrador ingresa a la url "http://localhost:8000/admin"')
def step_impl(context):
    context.driver.get("http://localhost:8000/admin")

@when('navega en la página de usuarios')
def step_impl(context):
    context.driver.find_element_by_link_text("Usuarios").click()

@then('el administrador debería ver la lista de todos los usuarios')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//table[@id='result_list']"))
    )
    user_list = context.driver.find_element_by_xpath("//table[@id='result_list']")
    assert user_list.text != ""

@given('el administrador ha iniciado sesión en el panel de administración')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:8000/admin")
    username_input = context.driver.find_element_by_name("username")
    password_input = context.driver.find_element_by_name("password")
    username_input.send_keys("tu_usuario")
    password_input.send_keys("tu_contraseña")
    context.driver.find_element_by_name("login").click()

@when('el administrador está en la página de usuarios')
def step_impl(context):
    context.driver.find_element_by_link_text("Usuarios").click()

@when('el administrador hace clic en un usuario')
def step_impl(context):
    user_list = context.driver.find_elements_by_xpath("//table[@id='result_list']//tr")
    user_list[1].find_element_by_tag_name("a").click()

@then('el administrador debería ver los detalles de ese usuario')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[@id='change-form']"))
    )
    user_details = context.driver.find_element_by_xpath("//h1[@id='change-form']")
    assert user_details.text != ""
