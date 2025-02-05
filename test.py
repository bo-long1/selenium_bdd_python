from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Khởi tạo WebDriver sử dụng WebDriverManager
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get("https://www.google.com")
print(driver.title)
driver.quit()