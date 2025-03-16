import re
import allure # type: ignore
import subprocess
import os

from helpers.log_config import logger
from helpers.utils import take_screenshot

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

def before_step(context, step):
    logger.info(f"Running step: {step.name}")
    context.allure_step = allure.step(step.name)
    context.allure_step.__enter__()

def after_step(context, step):
    try:
        if step.status == "failed":
            safe_step_name = re.sub(r'[^\w\-_\. ]', '_', step.name)
            screenshot_path = take_screenshot(context, safe_step_name)

            # Add images to Allure Report
            with open(screenshot_path, "rb") as image_file:
                allure.attach(image_file.read(), name=safe_step_name, attachment_type=allure.attachment_type.PNG)
    finally:
        if hasattr(context, "allure_step"):
            context.allure_step.__exit__(None, None, None)

def after_scenario(context, scenario):
    if scenario.status == "passed":
        logger.info(f"[PASS] Scenario '{scenario.name}' passed! Going back.")
        if hasattr(context, "driver") and context.driver:
            context.driver.back()
    else:
        logger.error(f"[ERROR] Scenario '{scenario.name}' failed!")

def after_all(context):
    if hasattr(context, "driver") and context.driver:
        try:
            logger.info("[INFO] Test suite finished!")
            print("==> WebDriver terminated successfully!")
            context.driver.close()
            context.driver.quit()
        except Exception as e:
            logger.error(f"Error terminating WebDriver: {e}")
            raise
    
    results_dir = "reports/allure-results"
    report_dir = "reports/allure-report"
    allure_cmd = "allure.bat" if os.name == "nt" else "allure"
    subprocess.run([allure_cmd, "generate", results_dir, "-o", report_dir, "--clean"], check=True)
    print(f"✅ Allure Report created at: {report_dir}")
    # auto open allure report
    subprocess.Popen([allure_cmd, "open", report_dir])
