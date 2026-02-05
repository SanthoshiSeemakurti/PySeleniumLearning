"""
Mini Project # (Selenium)

// Locators - Find the Web elements with XPATH and use Fluent wait
// Open the URL https://app.vwo.com/#/login
// Find the Email id** and enter the email as admin@admin.com
// Find the Pass inputbox** and enter passwrod as admin.
// Find and Click on the submit button
// Verify that the error message is shown "_**Your email, password, IP address or location did not match"**_
"""
from multiprocessing.context import assert_spawning

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Positive Testcase: App.VWO.com Signup button verification.")
@allure.description("Verify that Free Trial button is clicked and Navigated to the next page.")
def test_selenium_vwo_free_trial_project3():
    driver = webdriver.Firefox()
    driver.get("https://app.vwo.com/#/login")
    print(driver.title)

    # Free trial
    """
    <a 
    href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage" 
    class="text-link Td(n)" 
    data-qa="bericafeqo" 
    vwo-html-translate="login:startFreeTrial">Start a free trial<
    /a>"""
    vwo_free_trail = driver.find_element(By. PARTIAL_LINK_TEXT, "Start")
    vwo_free_trail.click()

    # verification
    current_url = driver.current_url
    assert current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    # Sign up free trial page
    """
    <h1 
    class="M(0) Fw(600) Fz(--font-size-30)--xs Fz(--font-size-20)">
    Sign up for a full-featured trial        
    </h1>"""
    WebDriverWait(driver=driver ,timeout= 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Sign up for a full-featured trial')]")))
    all_links_page = driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links_page))
    for i in all_links_page:
        print(i.text)


    # quit the Browser
    driver.quit()