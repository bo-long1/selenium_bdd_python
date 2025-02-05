import os
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


from features.steps.creenshot_util import take_screenshot

@given('launch Chrome browser')
def step_impl(context):
    # service = Service(executable_path='./src/driver/chromedriver.exe')
    # context.driver = webdriver.Chrome(service=service)
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    # service = FirefoxService(executable_path=GeckoDriverManager().install())
    # context.driver=webdriver.Firefox(service=service)

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
    time.sleep(2)
    take_screenshot(context, "verify_login")

@then('I user must successfully login to the Dashboard page')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//h6[normalize-space()='Dashboard'])[1]"))
        )
        text = context.driver.find_element(By.XPATH, "(//h6[normalize-space()='Dashboard'])[1]").text
        assert text == "Dashboard"
    except AssertionError as e:
        take_screenshot(context, "verify_dashboard2")
        raise e
    finally:
        context.driver.quit()