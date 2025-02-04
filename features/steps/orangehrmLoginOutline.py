import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when('open OrangeHRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)

@when('I Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.XPATH, "(//div[@class='oxd-input-group oxd-input-field-bottom-space'])[1]//input").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)
    time.sleep(2)

@when('I Click on login btn')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

@then('I user must successfully login to the Dashboard page')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//h6[normalize-space()='Dashboard'])[1]"))
    )
    text = context.driver.find_element(By.XPATH, "(//h6[normalize-space()='Dashboard'])[1]").text
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
    else:
        context.driver.close()
        assert False, "Test Failed"