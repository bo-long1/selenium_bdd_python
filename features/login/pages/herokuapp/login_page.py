from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Wait up to 10s if the element does not exist yet.
        self.wait = WebDriverWait(driver, 10)

        # Define locators
        self.abtesting = (By.XPATH, "(//a[normalize-space()='A/B Testing'])123")
        self.authentication = (By.XPATH, "//a[normalize-space()='Form Authentication']")
        self.username = (By.XPATH, "//input[@id='username']")
        self.password = (By.XPATH, "//input[@id='password']")
        self.btnlogin = (By.XPATH, "//i[@class='fa fa-2x fa-sign-in']")
        self.subheader = (By.CLASS_NAME, "subheader")
        self.basicauthen = (By.XPATH, "//a[normalize-space()='Basic Auth']")
        self.message = (By.XPATH, "//p[contains(text(),'Congratulations! You must have the proper credenti')]")

    def click_AB_testing (self):
        self.driver.find_element(*self.abtesting).click()

    def click_basic_authen (self):
        self.driver.find_element(*self.basicauthen).click()
    
    def handle_auth_popup(self, url):
        self.driver.get(url)

    def get_message (self):
        return self.wait.until(EC.presence_of_element_located(self.message)).text
    
    def click_login_authentication (self):
        self.driver.find_element(*self.authentication).click()

    def input_username_and_pwd (self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
    
    def click_btn_login (self):
        self.driver.find_element(*self.btnlogin).click()

    def verify_subheader (self):
        return self.wait.until(EC.presence_of_element_located(self.subheader)).text

class BasicAuthPage(LoginPage):
    def login_with_basic_auth(self, username, password, url):
        auth_url = f"https://{username}:{password}@{url}"  
        self.handle_auth_popup(auth_url)