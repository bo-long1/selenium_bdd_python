from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Wait up to 10s if the element does not exist yet.
        self.wait = WebDriverWait(driver, 10)

        # Define locators
        self.abtesting = (By.XPATH, "(//a[normalize-space()='A/B Testing'])[1]")
        self.authentication = (By.XPATH, "//a[normalize-space()='Form Authentication']")
        self.username = (By.XPATH, "//input[@id='username']")
        self.password = (By.XPATH, "//input[@id='password']")
        self.btnlogin = (By.XPATH, "//i[@class='fa fa-2x fa-sign-in']")
        self.subheader = (By.CLASS_NAME, "subheader")

    def click_AB_testing (self):
        self.driver.find_element(*self.abtesting).click()

    def click_login_authentication (self):
        self.driver.find_element(*self.authentication).click()

    def input_username_and_pwd (self):
        self.driver.find_element(*self.username).send_keys("tomsmith")
        self.driver.find_element(*self.password).send_keys("SuperSecretPassword!")
    
    def click_btn_login (self):
        self.driver.find_element(*self.btnlogin).click()

    def verify_subheader (self):
        return self.wait.until(EC.presence_of_element_located(self.subheader)).text