import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when('I open OrangeHRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("passed step open browser")
    time.sleep(2)

@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.XPATH, "(//div[@class='oxd-input-group oxd-input-field-bottom-space'])[1]//input").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)
    time.sleep(2)
    print("passed step input user pwd")

@when('Click on login btn')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

@then('user must successfully login to the Dashboard page')
def step_impl(context):
    # Add timeout to ensure element is ready
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//h6[normalize-space()='Dashboard'])[1]"))
    )
    text = context.driver.find_element(By.XPATH, "(//h6[normalize-space()='Dashboard'])[1]").text
    assert text == "Dashboard"
    context.driver.close()