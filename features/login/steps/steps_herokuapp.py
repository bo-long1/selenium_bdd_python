import sys
import os
import time
from behave import *
# from selenium.webdriver.common.by import By
from features.login.pages.herokuapp.login_page import BasicAuthPage

# Add path to helpers/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from helpers.webdriver_helper import get_login_page

# Add sys.path to import environment.py
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_dir)

# Import environment.py
import environment

@given('Open the browser')
def step_impl(context):
    # Gọi before_all để khởi tạo WebDriver
    environment.before_all(context)

@when('go to practice test page herokuapp')
def step_impl(context):
    # Open website from JSON config
    context.driver.get(environment.load_config().get("base_url"))

"""Scenario 1: Example scenario click into the func a/b testing"""
@when('click a/b testing')
# def step_impl(context):
#     element = context.browser.find_element(By.XPATH, "(//a[normalize-space()='A/B Testing'])[1]")
#     element.click()
def step_impl(context):
    get_login_page(context).click_AB_testing()
    time.sleep(2)

@then('should see the title "The Internet"')
def step_impl(context, title = "The Internet"):
    assert get_login_page(context).driver.title == title
    context.driver.close()

"""Scenario 2: test basic authentication"""
@when('Click to verify basic functionality')
def step_impl(context):
    get_login_page(context).click_basic_authen()

@when('input username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.auth_page = BasicAuthPage(context.driver)
    context.auth_page.login_with_basic_auth(username, password, "the-internet.herokuapp.com/basic_auth")

@then('Verify the authentication process')
def step_impl(context):
    assert get_login_page(context).get_message() == "Congratulations! You must have the proper credentials."

"""Scenario Outline 3: Click to the func Authentication"""
@when('click func Authentication')
def step_impl(context):
    get_login_page(context).click_login_authentication()

@when('input into the username "{username}" and password "{password}"')
def step_impl(context, username, password):
    get_login_page(context).input_username_and_pwd(username, password)

@when('enter button login')
def step_impl(context):
    get_login_page(context).click_btn_login()

@then('Verify user login success')
def step_impl(context):
    assert get_login_page(context).verify_subheader() == "Welcome to the Secure Area. When you are done click logout below."
    # context.driver.back()