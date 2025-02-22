import os
from datetime import datetime
import re

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
    if not os.path.exists("allure-results"):
        os.makedirs("allure-results")

def after_step(context, step):
    if step.status == "failed":
        safe_step_name = re.sub(r'[^\w\-_\. ]', '_', step.name)  # Remove special characters by lib re
        take_screenshot(context, safe_step_name)

def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()

