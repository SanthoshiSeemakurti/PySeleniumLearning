"""
## **Project 1 - Automating by using the Selenium Python. **
# 1. Navigate to the URL - [katalon-demo-cura.herokuapp.com](https://katalon-demo-cura.herokuapp.com/profile.php#login)
# 2. Find the **Make appointment** Button
# 3. Click on the **Make appointment **Button
# 4. Next Page will be loaded
# 5. **Find and Enter **the details **Username and Password** and **Click** on the Login Button
# 6. Verify current URL - [katalon-demo-cura.herokuapp.com/#appointment](https://katalon-demo-cura.herokuapp.com/#appointment)

"""
import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@allure.title("Katalon login Positive Testcase")
@allure.description(" Verify current URL - [katalon-demo-cura.herokuapp.com/#appointment]")
def test_project_1_katalon_login_positive():

    # Initialize ChromeOptions
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the URL
    driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
    print(driver.title)

    # click Make appointment
    """
    a 
    id="btn-make-appointment"
     href="./profile.php#login" 
     class="btn btn-dark btn-lg"
     >Make Appointment</a
    """
    appointmentButton = driver.find_element(By.ID, "btn-make-appointment")
    appointmentButton.click()

    # Username
    """<input 
    type="text" 
    class="form-control" 
    id="txt-username" 
    name="username" 
    placeholder="Username" 
    value="" 
    autocomplete="off">"""
    usernameInput = driver.find_element(By.NAME, "username" )
    usernameInput.send_keys("John Doe")

    # Password
    """
    <input 
    type="password" 
    class="form-control" 
    id="txt-password" 
    name="password" 
    placeholder="Password" 
    value="" 
    autocomplete="off">
    """
    passwordInput = driver.find_element(By.ID,"txt-password" )
    passwordInput.send_keys("ThisIsNotAPassword")
    time.sleep(3)
   

    # Click Login
    """
    <button 
    id="btn-login"
    type="submit"
    class="btn btn-default"
    >Login</button>
    """

    signin_Button = driver.find_element(By.ID, "btn-login")
    signin_Button.click()
    time.sleep(3)

    # Verify current URL
    appointmentPageUrl= driver.current_url
    assert appointmentPageUrl == "https://katalon-demo-cura.herokuapp.com/#appointment"
    print("Current URL: ",appointmentPageUrl)

    time.sleep(3)
    driver.quit()

    """
    Default Locators: ID, ClassName, LinkText, Partial Text, TagName.
    Advanced Locators - CSS (Custom- attribute), XPATH

    Preference Rule to find the element:
    Unique ID -> name-> class name-> link text/partial(a tag) - css selector -> Xpath

     If it is dynamic or changes, we try to avoid the locator or multiple classes. -> id = "30120225thy" 
     -> if it is not unique we will avoid it.
     Xpath , ss selector -> try to find the shortest locator and eas to remember, which doesn't change much.
    """