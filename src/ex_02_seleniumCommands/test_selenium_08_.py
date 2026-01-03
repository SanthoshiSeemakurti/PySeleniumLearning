import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_chrome_option():

    # Initialize ChromeOptions
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920x1080")  # Example option to run Chrome in headless mode

    driver = webdriver.Chrome(chrome_options)

    # Your test code here (for example, navigate to a page)
    driver.get("https://www..com")
    print(driver.title)
    time.sleep(10)
    driver.quit()