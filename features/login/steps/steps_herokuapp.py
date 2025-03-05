import time
from behave import *
from features.environment import *
from features.login.pages.herokuapp.login_page import BasicAuthPage
# Add path to helpers/
from helpers.webdriver_helper import get_login_page
# Import environment.py
import features.environment as environment
from helpers.config import load_config

@given('Open the browser')
def step_impl(context):
    pass

@when('go to practice test page herokuapp')
def step_impl(context):
    context.driver.get(load_config().get("base_url"))


"""Scenario 1: Example scenario click into the func a/b testing"""
@when('click a/b testing')
def step_impl(context):
    get_login_page(context).click_AB_testing()
    time.sleep(2)

@then('should see the title "The Internet"')
def step_impl(context, title = "The Internet"):
    assert get_login_page(context).driver.title == title

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
