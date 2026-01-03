"""
Mini Project #2 (Selenium)

// Locators - Find the Web elements
// Open the URL https://app.vwo.com/#/login
// Find the Email id** and enter the email as admin@admin.com
// Find the Pass inputbox** and enter passwrod as admin.
// Find and Click on the submit button
// Verify that the error message is shown "_**Your email, password, IP address or location did not match"**_
"""


import allure
import pytest
from selenium import webdriver


@allure.title("Login to VWO")
@allure.description("Find the Web elements on the page")
def selenium_test_VWO_login():
    driver = webdriver.Firefox()
    driver.get("https://app.vwo.com/#/login")
    print(driver.title)
    driver.get_id : "login-username"





