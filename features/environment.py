import os
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from features.pages.herokuapp.login_page import LoginPage

def take_screenshot(context, step_name):
    try:
        if not hasattr(context, "driver") or context.driver is None:
            print("❌ Driver is not initialized, skipping screenshot.")
            return

        # Create directory
        screenshots_dir = f"screenshots/{datetime.now().strftime('%Y-%m-%d')}"
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

def before_all(context):
    """Khởi tạo WebDriver một lần duy nhất khi bắt đầu chạy test"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # on mode headless
    chrome_options.add_argument("--disable-gpu")  # More stable on Windows
    chrome_options.add_argument("--no-sandbox") # Run without root privileges (useful on Linux)
    chrome_options.add_argument("--disable-dev-shm-usage") # Helps reduce errors on Docker/Linux

    #context.driver = webdriver.Firefox()
    #context.driver = webdriver.Edge()
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    print("🚀 WebDriver initialized!")

def before_scenario(context, scenario):
    """Open the web page before each scenario"""
    base_url = "https://the-internet.herokuapp.com/"
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


