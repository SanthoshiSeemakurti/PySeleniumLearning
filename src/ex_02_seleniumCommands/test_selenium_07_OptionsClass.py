"""
Mini Project #1 (Selenium)

// Locators - Find the Web elements
// Open the URL 'https://katalon-demo-cura.herokuapp.com'
// Find page source: "CURA Healthcare Service" in page_source_as_html
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


# driver = webdriver.Chrome(ChromeDriverManager().install())
def test_chrome_option():


    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=1920x1080")
    # chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options= chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com")
    print(driver.title)
    time.sleep(5)
    driver.quit()