import re
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# Add path to helpers/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from helpers.config import load_config
from helpers.utils import take_screenshot


def before_all(context):
    config = load_config()
    browser = config.get("browser", "chrome").lower()  # Get browser configuration from JSON, default is chrome
    headless_mode = config.get("headless", False) # Read headless option (default is False)

    chrome_options = Options()
    firefox_options = FirefoxOptions()
    edge_options = EdgeOptions()

    #headless mode
    if headless_mode:
        print("Running browser in headless mode!")
        chrome_options.add_argument("--headless")
        firefox_options.add_argument("--headless")
        edge_options.add_argument("--headless")
        #headless options
        chrome_options.add_argument("--disable-gpu")  # More stable on Windows
        chrome_options.add_argument("--no-sandbox") # Run without root privileges (useful on Linux)
        chrome_options.add_argument("--disable-dev-shm-usage") # Helps reduce errors on Docker/Linux

        firefox_options.add_argument("--disable-gpu")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")

        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")

    # Initialize WebDriver based on browser selection
    if browser == "chrome":
        context.driver = webdriver.Chrome(options=chrome_options)
    elif browser == "firefox":
        context.driver = webdriver.Firefox(options=firefox_options)
    elif browser == "edge":
        context.driver = webdriver.Edge(options=edge_options)
    else:
        print(f"Unsupported browser: {browser}, defaulting to Chrome.")
        context.driver = webdriver.Chrome(options=chrome_options)

    context.driver.maximize_window()
    print(f"WebDriver initialized with {browser.capitalize()}!")

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


