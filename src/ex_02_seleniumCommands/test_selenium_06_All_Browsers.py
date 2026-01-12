"""
Mini Project #(Selenium) - parallel testing

// Locators - Find the Web elements
// Open the URL 'https://katalon-demo-cura.herokuapp.com'
// Find page source: "CURA Healthcare Service" in page_source_as_html
"""

import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@allure.title("Print the page source in katalon page in Firefox browser")
def test_selenium_Ffirefox_Browser():
    driver = webdriver.Firefox()
    driver.get('https://katalon-demo-cura.herokuapp.com')
    print(driver.title)
    print(driver.current_url)
    pageSource = driver.page_source
    assert "CURA Healthcare Service" in pageSource
    time.sleep(1)
    driver.quit()

@allure.title("Print the page source in katalon page in chrome browser")
def test_selenium_chrome_Browser():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://katalon-demo-cura.herokuapp.com')
    print(driver.title)
    print(driver.current_url)
    pageSource = driver.page_source
    assert "CURA Healthcare Service" in pageSource
    time.sleep(1)
    driver.quit()

@allure.title("Print the page source in katalon page in edge browser")
def test_selenium_edge_Browser():
    driver = webdriver.Edge()
    driver.get('https://katalon-demo-cura.herokuapp.com')
    print(driver.title)
    print(driver.current_url)
    pageSource = driver.page_source
    assert "CURA Healthcare Service" in pageSource
    time.sleep(1)
    driver.quit()

@allure.title("Print the page source in katalon page in safari browser")
def test_selenium_safari_Browser():
    driver = webdriver.Safari()
    driver.get('https://katalon-demo-cura.herokuapp.com')
    print(driver.title)
    print(driver.current_url)
    pageSource = driver.page_source
    assert "CURA Healthcare Service" in pageSource
    time.sleep(1)
    driver.quit()

    # to run the testcases parallel, need to install: pip install pytest-xdist
    # to run: pytest -n auto src/ex_02_seleniumCommands/test_selenium_06_All_Browsers.py
