import re
import shutil
import allure  # type: ignore
import os
from helpers.webdriver_helper import get_login_page
from helpers.config import load_config
from helpers.log_config import logger
from helpers.screenshot import take_screenshot
from helpers.allure_report import generate_allure_report, open_allure_report
from driver.BrowserType import headless_mode


def before_all(context):
    logger.info("Starting the test suite...")
    logger.info(f"Browser opened and navigated to: {load_config().get("base_url")}")
    with allure.step("Initialize WebDriver!"):
        headless_mode(context) # Initialize the WebDriver in headless mode

    results_dir = "allure-results"
    # Safely recreate the results directory
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir) # Remove the directory and all its contents
    os.makedirs(results_dir, exist_ok=True) # Create the directory if it doesn't exist
    os.environ["ALLURE_RESULTS_DIR"] = results_dir # Set the environment variable

def before_scenario(context, scenario):
    """
    This hook runs before every scenario.
    It navigates to the practice test page using an existing browser instance.
    """
    logger.info("Starting scenario: %s", scenario.name)

    # Navigate to the base URL
    base_url = load_config().get("base_url")
    context.driver.get(base_url)
    logger.info("Navigated to: %s", base_url)

def after_step(context, step):
    if step.status == "failed":
        safe_step_name = re.sub(r'\W+', '_', step.name)  # Stricter sanitization
        screenshot_path = take_screenshot(context, safe_step_name)

        # Attach screenshot to Allure report
        try:
            with open(screenshot_path, "rb") as image_file:
                allure.attach(image_file.read(), name=safe_step_name, attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            logger.error(f"Failed to attach screenshot: {e}")

def after_all(context):
    if hasattr(context, "driver") and getattr(context, "driver"):
        logger.info("Test suite finished!")
        context.driver.quit()
        generate_allure_report()

