import time
from behave import *
from selenium.webdriver.common.by import By

from features.login.pages.herokuapp import BasicAuthPage

@given('Open the browser')
def step_impl(context):
    pass

@when('go to practice test page herokuapp')
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

@when('Click to verify basic functionality')
def step_impl(context):
    context.login_page.click_basic_authen()

@when('input username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.auth_page = BasicAuthPage(context.driver)
    context.auth_page.login_with_basic_auth(username, password, "the-internet.herokuapp.com/basic_auth")

@then('Verify the authentication process')
def step_impl(context):
    assert context.login_page.get_message() == "Congratulations! You must have the proper credentials."

@when('click func Authentication')
def step_impl(context):
    context.login_page.click_login_authentication()

@when('input into the username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.input_username_and_pwd(username, password)

@when('enter button login')
def step_impl(context):
    context.login_page.click_btn_login()

@then('Verify user login success')
def step_impl(context):
    assert context.login_page.verify_subheader() == "Welcome to the Secure Area. When you are done click logout below."
    context.driver.back()