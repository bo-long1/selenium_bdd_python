import os
import re
from datetime import datetime

def take_screenshot(context, step_name):
    try:
        # Create directory 
        screenshots_dir = os.path.join("reports", "screenshots", datetime.now().strftime('%Y-%m-%d'))
        if not os.path.exists(screenshots_dir):
            print(f"==> Creating directory: {screenshots_dir}")
            os.makedirs(screenshots_dir)

        # Process step names to avoid special characters
        safe_step_name = re.sub(r'[^\w\-_\. ]', '_', step_name)
        screenshot_file = os.path.join(screenshots_dir, f"{safe_step_name}.png")

        # Take screenshot from WebDriver (context.driver)
        if context.driver.save_screenshot(screenshot_file):
            print(f"==> Screenshot saved: {screenshot_file}")
        else:
            print("==> Failed to save screenshot.")

    except Exception as e:
        print(f"Error while saving screenshot: {e}")
