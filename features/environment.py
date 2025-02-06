import allure
import os
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def take_screenshot(context, step_name, screenshots_dir="/screenshots"):
    try:
        # Create directory
        screenshots_dir = f"screenshots/{datetime.now().strftime('%Y-%m-%d')}"
        if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)

        # Screenshots
        screenshot_file = os.path.join(screenshots_dir, f"{step_name}.png")
        context.driver.save_screenshot(screenshot_file)
        
    except Exception as e:
        print(f"Error while saving screenshot: {e}")

def before_all(context):
    if not os.path.exists("allure-results"):
        os.makedirs("allure-results")

def after_step(context, step):
    if step.status == "failed":
        take_screenshot(context, step.name)

def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()

