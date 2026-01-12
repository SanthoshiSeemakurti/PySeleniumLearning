"""
Mini Project #3 (Selenium)

// Locators - Find the Web elements
// Open the URL 'www.idrive360.com/enterprise/account?upgradenow=true'
// Login to the page, Email:augtest_040823@idrive.com,  Password: 123456
// Find : "Your free trial has expired!" in page_source_as_html
"""

import time
from typing import Any

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

@allure.title("IDRVE login Positive Testcase")
@allure.description(" Verify 'Your free trial has expired!' in page_source_as_html")
def test_verify_idrive_upgrade_message():

    # initialize chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    # navigate to idrive360 page
    driver.get("https://www.idrive360.com/enterprise/account?upgradenow=true")
    time.sleep(3)

    # Login
    """
    <input _ngcontent-ige-c171="" 
    type="email" 
    id="username" 
    name="username" 
    autofocus="" 
    class="id-form-ctrl ng-pristine ng-valid ng-touched">
    """
    email_placeholder= driver.find_element(By.ID, "username")
    email_placeholder.send_keys("augtest_040823@idrive.com")

    # password
    """<input _ngcontent-ige-c171="" 
    id="password" 
    name="password" 
    tabindex="0" 
    maxlength="20" 
    class="id-form-ctrl ng-untouched ng-pristine ng-valid" 
    type="password">
    """
    password_placeholder= driver.find_element(By.NAME, "password")
    password_placeholder.send_keys("123456")

    # login
    """<button _ngcontent-bhl-c171="" 
    type="submit" 
    id="frm-btn" 
    class="id-btn id-info-btn-frm">Sign in</button>"""
    signin_button = driver.find_element(By.ID, "frm-btn")
    signin_button.click()
    time.sleep(5)
    WebDriverWait(driver, 20)

    # upgrade_message

    """
    <div _ngcontent-kee-c141="" 
    id="expiredmsg" 
    class="id-card-blk id-expire-msg id-expire-msg-nw failure"
    ><div 
        _ngcontent-kee-c141="" 
        class="id-card-cont">
        <i _ngcontent-kee-c141="" 
        class="id-expire-msg-icon"></i>
        <h5 _ngcontent-kee-c141="" 
        class="id-card-title">Your free trial has expired!</h5>
        <p _ngcontent-kee-c141="">Your free trial account has expired. To continue using the service, please choose one of our paid plans.</p><p _ngcontent-kee-c141="">As a special offer for you, we are giving 90% off on the first year of your subscription.</p></div></div>
    """
    upgrade_message= driver.find_element(By.ID, "expiredmsg")
    assert "Your free trial account has expired. To continue using the service, please choose one of our paid plans." in upgrade_message.text
    time.sleep(3)
    driver.quit()
