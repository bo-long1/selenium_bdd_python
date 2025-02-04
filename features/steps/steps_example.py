import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('Open the browser')
def step_impl(context):
    context.browser = webdriver.Chrome()
    #context.browser = webdriver.Firefox()
    #context.browser = webdriver.Edge()
    context.browser.maximize_window()

@when('go to practice test page "https://the-internet.herokuapp.com/"')
def step_impl(context):
    context.browser.get("https://the-internet.herokuapp.com/")

@when('click a/b testing')
def step_impl(context):
    element = context.browser.find_element(By.XPATH, "(//a[normalize-space()='A/B Testing'])[1]")
    element.click()

@then('should see the title "The Internet"')
def step_impl(context, title = "The Internet"):
    assert context.browser.title == title
    time.sleep(2)
    context.browser.quit()
