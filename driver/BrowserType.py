from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from helpers.config import load_config

def headless_mode(context):
    config = load_config()  # Lấy cấu hình từ helpers/config.py
    browser = config.get("browser").lower()  # Default là Chrome nếu không có
    headless = config.get("headless", False)

    # Initialize browser-based options
    options_map = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
    }
    options = options_map.get(browser)
    if not options:
        raise ValueError(f"Unsupported browser: {browser}")

    # If running headless mode, add general options
    if headless:
        print(f"🚀 Running {browser.capitalize()} in headless mode!")
        for arg in ["--headless", "--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage"]:
            options.add_argument(arg)

    # Initialize WebDriver
    driver_map = {
        "chrome": webdriver.Chrome,
        "firefox": webdriver.Firefox,
        "edge": webdriver.Edge,
    }
    context.driver = driver_map.get(browser)(options=options)
    context.driver.maximize_window()
    print(f"==> WebDriver initialized with {browser.capitalize()}!")
