import os
import re
from datetime import datetime

def take_screenshot(driver, step_name):
    try:
        if driver is None:
            print("❌ Driver is not initialized, skipping screenshot.")
            return

        # Create directory for screenshots
        screenshots_dir = os.path.join("reports", "screenshots", datetime.now().strftime('%Y-%m-%d'))
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        # Capture screenshot
        screenshot_file = os.path.join(screenshots_dir, f"{step_name}.png")
        if driver.save_screenshot(screenshot_file):
            print(f"✅ Screenshot saved: {screenshot_file}")
        else:
            print("❌ Failed to save screenshot.")

    except Exception as e:
        print(f"⚠️ Error while saving screenshot: {e}")
