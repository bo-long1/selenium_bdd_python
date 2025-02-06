from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument("--headless")  # Chạy ẩn
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

service = ChromeService(ChromeDriverManager().install())  # Đảm bảo đường dẫn chính xác
driver = webdriver.Chrome(service=service, options=chrome_options)

# Mở trang web
driver.get("https://www.google.com")



# Chụp màn hình
driver.save_screenshot("screenshot.png")

driver.quit()
