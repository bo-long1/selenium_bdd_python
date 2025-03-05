import re
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# Add path to helpers/
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from helpers.config import load_config
from helpers.utils import take_screenshot


def before_all(context):
    config = load_config()
    browser = config.get("browser", "chrome").lower()
    headless_mode = config.get("headless", False)

    # Initialize browser-based options
    options_map = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
    }
    options = options_map.get(browser, ChromeOptions())

    # If running headless mode, add general options
    if headless_mode:
        print("🚀 Running browser in headless mode!")
        for arg in ["--headless", "--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage"]:
            options.add_argument(arg)

    # Initialize WebDriver
    driver_map = {
        "chrome": webdriver.Chrome,
        "firefox": webdriver.Firefox,
        "edge": webdriver.Edge,
    }
    context.driver = driver_map.get(browser, webdriver.Chrome)(options=options)

    context.driver.maximize_window()
    print(f"✅ WebDriver initialized with {browser.capitalize()}!")

def after_step(context, step):
    if step.status == "failed":
        safe_step_name = re.sub(r'[^\w\-_\. ]', '_', step.name)  # Remove special characters
        take_screenshot(context, safe_step_name)

def after_all(context):
    if hasattr(context, "driver") and context.driver:
        try:
            context.driver.quit()
            print("==> WebDriver terminated successfully!")
        except Exception as e:
            print(f"==> Error terminating WebDriver: {e}")


