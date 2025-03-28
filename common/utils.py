from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class Utils:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=0.5, ignored_exceptions=[NoSuchElementException])

    def click_element(self, locator):
        """Wait for an element to be clickable and click it."""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise Exception(f"Element with locator {locator} not clickable after timeout.")

    def send_keys_to_element(self, locator, keys):
        """Wait for an element to be visible and send keys to it."""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.send_keys(keys)
        except TimeoutException:
            raise Exception(f"Element with locator {locator} not visible after timeout.")

    def get_element_text(self, locator):
        """Wait for an element to be visible and return its text."""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            raise Exception(f"Element with locator {locator} not visible after timeout.")

    def wait_for_element(self, locator):
        """Wait for an element to be present in the DOM."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element with locator {locator} not present after timeout.")