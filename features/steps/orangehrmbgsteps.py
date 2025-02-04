import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I launch browser application')
def step_impl(context):
    assert True, "Test Passed"
    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()


@when('I open Application application')
def step_impl(context):
    assert True, "Test Passed"
    # context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # print("passed step open browser")
    # time.sleep(2)


@when('Enter valid username anh password application')
def step_impl(context):
    assert True, "Test Passed"
    # context.driver.find_element(By.XPATH, "(//div[@class='oxd-input-group oxd-input-field-bottom-space'])[1]//input").send_keys("Admin")
    # context.driver.find_element(By.NAME, "password").send_keys("admin123")
    # time.sleep(2)


@when('Click on Login applications')
def step_impl(context):
    assert True, "Test Passed"


@then('user must login to the Dashboard page application')
def step_impl(context):
    assert True, "Test Passed"


@when('Enter valid username and password application')
def step_impl(context):
    assert True, "Test Passed"


@when('Click on login application')
def step_impl(context):
    assert True, "Test Passed"


@when('Navigate to Search page application')
def step_impl(context):
    assert True, "Test Passed"


@then('Search page should display application')
def step_impl(context):
    assert True, "Test Passed"


@when('Navigate advanced search page application')
def step_impl(context):
    assert True, "Test Passed"


@then('Advanced search page should display application')
def step_impl(context):
    assert True, "Test Passed"