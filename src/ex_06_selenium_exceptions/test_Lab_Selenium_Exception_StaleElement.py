import allure
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By


"""
stale element exception is generally occurs when the page is refreshed, page is changed, DOM section or XTML is changed 
stale means old, not fresh 
"""
@allure.title("Exception handling")
@allure.description("Verify stale exception_handling")
def test_stale_element_exceptions():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    time.sleep(3)
    """
    <textarea 
    id="input" 
    autocomplete="off" 
    part="searchbox-input" 
    spellcheck="false" 
    role="combobox" 
    aria-controls="matches" 
    aria-live="polite" 
    aria-expanded="false" 
    aria-description="" 
    placeholder="Ask about a tab"
    ></textarea>
    """

    try:
        text_area = driver.find_element(By.XPATH, "//textarea[@role='combobox']")
        text_area.send_keys("qa test")
        driver.refresh()
        time.sleep(2)
        text_area.send_keys("qa")
        time.sleep(2)
    except StaleElementReferenceException as see:
        print(see.msg)

    driver.quit()
