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
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Negative Testcase: App.VWO.com - wrong credentials -> Error message.")
@allure.description("Verify that if user credentials are wrong and error message is shown.")
def test_selenium_VWO_invalid_login():
    driver = webdriver.Firefox()
    driver.get("https://app.vwo.com/#/login")
    print(driver.title)

    # Login
    loginVWO =driver.find_element(By.XPATH, "//input[@id='login-username']")
    loginVWO.send_keys("admin")

    # Password
    passwordVWO =driver.find_element(By.XPATH, "//input[@id='login-password']")
    passwordVWO.send_keys("123456789")

    # Login button
    """
    <button type="submit" 
    id="js-login-btn" 
    class="btn btn--primary btn--inverted W(100%) Mb(8px) Mb(0):lc" 
    onclick="login.login(event)" 
    data-qa="sibequkica"
    > <span 
    class="icon loader hidden" 
    data-qa="zuyezasugu"
    ></span> <span 
    data-qa="ezazsuguuy" 
    vwo-html-translate="login:signIn"
    >Sign in</span>
     </button>"""
    loginButtonVWO = driver.find_element(By.XPATH, "//button[@onclick='login.login(event)']")
    loginButtonVWO.click()

    # Fluent wait: Checks the web element visibility with the time interval i.e., poll frequency
    WebDriverWait(driver = driver, poll_frequency=1, timeout = 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='js-notification-box']")))

    # Notification box
    """<div 
       class="notification-box notification-box--filled notification-box--warning P(10px) Mb(20px)" 
       id="js-notification-box" 
       data-qa="tozemoxine"
      """
    notification_message = driver.find_element(By.XPATH, "//div[@id='js-notification-box']")

    # verification
    assert "Your email, password, IP address or location did not match" in notification_message.text

    # quit the Browser
    driver.quit()