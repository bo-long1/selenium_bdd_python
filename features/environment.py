import re
from helpers.log_config import logger
from helpers.utils import take_screenshot
from driver.BrowserType import headless_mode

def before_all(context):
    try:
        logger.info("[INFO] Starting the test suite...")
        headless_mode(context)
    except Exception as e:
        print(f"==> Error terminating WebDriver: {e}")


def after_step(context, step):
    if step.status == "failed":
        safe_step_name = re.sub(r'[^\w\-_\. ]', '_', step.name)  # Remove special characters
        take_screenshot(context, safe_step_name)


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
            context.driver.quit()
        except Exception as e:
            print(f"==> Error terminating WebDriver: {e}")


