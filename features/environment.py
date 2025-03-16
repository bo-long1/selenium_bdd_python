import re
import allure  # type: ignore
import os

from helpers.log_config import logger
from helpers.screenshot import take_screenshot
from helpers.allure_report import generate_allure_report, open_allure_report
from driver.BrowserType import headless_mode

def before_all(context):
    logger.info("[INFO] Starting the test suite...")
    with allure.step("Initialize WebDriver!"):
        headless_mode(context)
    results_dir = "reports/allure-results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    os.environ["ALLURE_RESULTS_DIR"] = results_dir
    logger.info(f"✅ Allure results will be saved at: {results_dir}")

def after_step(context, step):
    if step.status == "failed":
        safe_step_name = re.sub(r'[^\w\-_\. ]', '_', step.name)
        screenshot_path = take_screenshot(context, safe_step_name)

        # Attach screenshot to Allure report
        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name=safe_step_name, attachment_type=allure.attachment_type.PNG)

def after_all(context):
    if hasattr(context, "driver") and context.driver:
        try:
            logger.info("[INFO] Test suite finished!")
            context.driver.quit()
        except Exception as e:
            logger.error(f"Error terminating WebDriver: {e}")

    # Generate & Open Allure Report
    report_dir = generate_allure_report()
    if report_dir:
        open_allure_report(report_dir)
