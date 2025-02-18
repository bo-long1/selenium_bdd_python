import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@given('Open the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    #context.browser = webdriver.Firefox()
    #context.browser = webdriver.Edge()
    context.driver.maximize_window()

@when('go to practice test page "https://the-internet.herokuapp.com/"')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.login_page = LoginPage(context.driver)

@when('click a/b testing')
# def step_impl(context):
#     element = context.browser.find_element(By.XPATH, "(//a[normalize-space()='A/B Testing'])[1]")
#     element.click()
def step_impl(context):
    context.login_page.click_AB_testing()
    time.sleep(2)

@then('should see the title "The Internet"')
def step_impl(context, title = "The Internet1"):
    assert context.driver.title == title
    time.sleep(2)