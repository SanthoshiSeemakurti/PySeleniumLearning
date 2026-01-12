"""
## **Project 1 - Automating by using the Selenium Python. **
# 1. Navigate to the URL - [katalon-demo-cura.herokuapp.com](https://katalon-demo-cura.herokuapp.com/profile.php#login)
# 2. Find the **Make appointment** Button
# 3. Click on the **Make appointment **Button
# 4. Next Page will be loaded
# 5. **Find and Enter **Wrong  details **Username and Password** and **Click** on the Login Button
# 6. Verify the current Error message.
"""
import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@allure.title("Katalon login negative Testcase")
@allure.description("Verify Error message on the login page")
def test_project_1_katalon_login_negative():

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
    usernameInput.send_keys("Zara")

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
    passwordInput.send_keys("Password")
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
    time.sleep(1)

    # Verify error message
    """
    class="lead text-danger"
    >Login failed! Please ensure the username and password are valid.<
    """
    errorMessage_p_tag = driver.find_element(By.CLASS_NAME, "text-danger")
    assert  "Login failed! Please ensure the username and password are valid."== errorMessage_p_tag.text

    time.sleep(1)
    driver.quit()
