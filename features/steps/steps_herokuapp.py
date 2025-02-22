import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Open the browser')
def step_impl(context):
    pass

@when('go to practice test page "https://the-internet.herokuapp.com/"')
def step_impl(context):
    pass

@when('click a/b testing')
# def step_impl(context):
#     element = context.browser.find_element(By.XPATH, "(//a[normalize-space()='A/B Testing'])[1]")
#     element.click()
def step_impl(context):
    context.login_page.click_AB_testing()
    time.sleep(2)

@then('should see the title "The Internet"')
def step_impl(context, title = "The Internet"):
    assert context.driver.title == title
    context.driver.back()

@when('click func Authentication')
def step_impl(context):
    context.login_page.click_login_authentication()

@when('input username and password')
def step_impl(context):
    context.login_page.input_username_and_pwd()

@when('enter button login')
def step_impl(context):
    context.login_page.click_btn_login()

@then('Verify user login success')
def step_impl(context):
    assert context.login_page.verify_subheader() == "Welcome to the Secure Area. When you are done click logout below."