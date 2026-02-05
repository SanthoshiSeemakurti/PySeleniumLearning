import time
from asyncio import timeout

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("SVG")
@allure.description("Verify svg")
def test_svg_js_alerts():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    """<input 
    class="nw1UBF v1zwn25" 
    type="text" 
    title="Search for Products, Brands and More" 
    name="q" 
    autocomplete="off" 
    placeholder="Search for Products, Brands and More" 
    value="" 
    style="color: rgb(61, 61, 61);"
    >
    """
    serchBox= driver.find_element(By.CSS_SELECTOR, value="input[name='q']")
    serchBox.send_keys("macmini")
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='q']")) )

    # Click on search svg (Svg can only found by Xpath)

    search_svg= driver.find_elements(By.XPATH, value="//*[name()='svg']")
    search_svg[0].click() # we have list of svgs, here we want to click first svg in the list
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//*[name()='svg']")))

    driver.quit()

    # Svg can only found by Xpath
    # logic to find list of svg://*[name()='svg']
