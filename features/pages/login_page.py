from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.abtesting = (By.XPATH, "(//a[normalize-space()='A/B Testing'])[1]")

    def click_AB_testing (self):
        self.driver.find_element(*self.abtesting).click()