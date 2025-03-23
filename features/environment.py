import re
import shutil
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

    # Safely recreate the results directory
    if os.path.exists(results_dir):
        try:
            shutil.rmtree(results_dir)
        except Exception as e:
            logger.error(f"Error removing Allure results directory: {e}")

    os.makedirs(results_dir, exist_ok=True)
    os.environ["ALLURE_RESULTS_DIR"] = results_dir

    logger.info(f"✅ Allure results will be saved at: {results_dir}")


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
    if hasattr(context, "driver") and getattr(context, "driver", None):
        try:
            logger.info("[INFO] Test suite finished!")
            context.driver.quit()
        except Exception as e:
            logger.error(f"Error terminating WebDriver: {e}")

    # Generate & Open Allure Report
    generate_allure_report()
    # report_dir = generate_allure_report()
    # if report_dir:
    #     open_allure_report(report_dir)
