import os
from datetime import datetime

def take_screenshot(context, step_name):
    screenshots_dir = os.path.join("reports", "screenshots", datetime.now().strftime('%Y-%m-%d'))
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    
    screenshot_path = os.path.join(screenshots_dir, f"{step_name}.png")
    context.driver.save_screenshot(screenshot_path)
    
    return screenshot_path
