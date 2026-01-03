import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
"""
Mini Project #1 (Selenium)
// Locators - Find the Web elements
// Open the URL https://app.vwo.com/#/login
// Find the Email id** and enter the email as admin@admin.com
// Find the Pass inputbox** and enter passwrod as admin.
// Find and Click on the submit button
// Verify that the error message is shown "_**Your email, password, IP address or location did not match"**_

"""

def test_chrome_option():

    # Initialize ChromeOptions
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920x1080")  # Example option to run Chrome in headless mode

    driver = webdriver.Chrome(chrome_options)

    # Your test code here (for example, navigate to a page)
    driver.get("https://app.vwo.com/#/login")
    print(driver.title)

    # Email Address placeholder:
    emailAddress= driver.find_element(By.NAME,"username")
    emailAddress.send_keys("admin@admin.com")

    """
     input type="email"
     class="text-input W(100%)" 
     name="username" 
     vwo-html-translate-attr="placeholder" 
     vwo-html-translate-placeholder="login:enterEmailID" 
     id="login-username" 
     data-qa="hocewoqisi" 
     placeholder="Enter email ID"
     """
    # password placeholder:

    password= driver.find_element(By.ID,"login-password")
    password.send_keys("admin")

    """
    input type="password" 
    class="text-input W(100%)" 
    vwo-html-translate-attr="placeholder" 
    vwo-html-translate-placeholder="login:enterPassword" 
    name="password" 
    id="login-password" 
    data-qa="jobodapuxe" 
    placeholder="Enter password"
    """

    # Signin button:
    """
    button type="submit" 
    id="js-login-btn" 
    class="btn btn--primary btn--inverted W(100%) Mb(8px) Mb(0):lc" 
    onclick="login.login(event)" 
    data-qa="sibequkica"
    > <span class="icon loader hidden" 
    data-qa="zuyezasugu"
    ></span> <span data-qa="ezazsuguuy" 
    vwo-html-translate="login:signIn"
    >Sign in</span> </button>"""

    # login button:
    login_button=driver.find_element(By.ID,"js-login-btn")
    login_button.click()
    time.sleep(3)

    # Error notification message:
    """<div class="notification-box-description" 
    id="js-notification-box-msg" 
    data-qa="rixawilomi"
    >Your email, password, IP address or location did not match</div"""

    errormessage= driver.find_element(By.ID,"js-notification-box-msg")
    assert "Your email, password, IP address or location did not match" == errormessage.text

    driver.quit()