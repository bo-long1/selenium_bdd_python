import json
import os
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from features.login.pages.herokuapp.login_page import LoginPage

def take_screenshot(context, step_name):
    try:
        if not hasattr(context, "driver") or context.driver is None:
            print("❌ Driver is not initialized, skipping screenshot.")
            return

        # Create directory
        screenshots_dir = os.path.join("reports", "screenshots", datetime.now().strftime('%Y-%m-%d'))
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        # Creenshot and check result
        screenshot_file = os.path.join(screenshots_dir, f"{step_name}.png")
        if context.driver.save_screenshot(screenshot_file):
            print(f"✅ Screenshot saved: {screenshot_file}")
        else:
            print("❌ Failed to save screenshot.")

        # export console logs file screenshot existed ?
        if os.path.exists(screenshot_file):
            print(f"📂 File exists: {screenshot_file}")
        else:
            print(f"⚠️ File does not exist after saving: {screenshot_file}")

    except Exception as e:
        print(f"⚠️ Error while saving screenshot: {e}")

def load_config():
    """Load configuration from a JSON file"""
    #config_path = './config/testsetting.json'  # Path to JSON file
    config_path = os.path.join("config","testsetting.json")
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        print(f"⚠️ Config file {config_path} not found.")
        return {}


def before_all(context):
    config = load_config()
    browser = config.get("browser", "chrome").lower()  # Get browser configuration from JSON, default is chrome
    headless_mode = config.get("headless", False) # Read headless option (default is False)

    chrome_options = Options()
    firefox_options = FirefoxOptions()
    edge_options = EdgeOptions()

    #headless mode
    if headless_mode:
        print("🔄 Running browser in headless mode...")
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
        print(f"⚠️ Unsupported browser: {browser}, defaulting to Chrome.")
        context.driver = webdriver.Chrome(options=chrome_options)

    context.driver.maximize_window()
    print(f"🚀 WebDriver initialized with {browser.capitalize()}!")

def before_scenario(context, scenario):
    """Open the web page before each scenario"""
    config = load_config()
    base_url = config.get("base_url")  # Get values ​​from JSON file
    context.driver.get(base_url)
    context.login_page = LoginPage(context.driver)  # Create object Page Object Model
    print(f"🌍 Opened page: {base_url}")

def after_step(context, step):
    if step.status == "failed":
        safe_step_name = re.sub(r'[^\w\-_\. ]', '_', step.name)  # Remove special characters by lib re
        take_screenshot(context, safe_step_name)

def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()


