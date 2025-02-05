from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from features.steps.creenshot_util import take_screenshot

# def before_all(context):
#     service = Service(executable_path='./src/driver/chromedriver.exe')
#     service = webdriver.Chrome(service=service)
#     context.driver.maximize_window()

# def after_all(context):
#     context.driver.quit()

def after_step(context, step):
    if step.status == "failed":
        take_screenshot(context, step.name)
