"""
Mini Project #1 (Selenium)

// Locators - Find the Web elements
// Open the URL 'https://katalon-demo-cura.herokuapp.com'
// Find page source: "CURA Healthcare Service" in page_source_as_html
"""


import allure
from selenium import webdriver


@allure.title("Print the page source in katalon page")
def test_selenium():
    driver = webdriver.Firefox()
    driver.get('https://katalon-demo-cura.herokuapp.com')
    print(driver.title)
    print(driver.current_url)
    pageSource = driver.page_source
    assert "CURA Healthcare Service" in pageSource
    driver.quit()
