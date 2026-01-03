import pytest
import allure
from selenium import webdriver


def test_selenium_01():
    driver = webdriver.Firefox()
    driver.get("https://thetestingacademy.com")
    print (driver.title)
    assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"

    driver.quit()
    """
    driver = webdriver is the core mechanism in Selenium for creating an instance of a specific web browser and assigning it to a variable called driver. 
    This driver object then acts as the programming interface you use to control the browser's behavior, 
    such as navigating to URLs, finding elements, and interacting with a web page.
     
   webdriver: This is a key interface (or class, depending on the language bindings) provided by the Selenium library. 
   It defines a common set of methods and properties for all browsers (like get(), findElement(), click(), getTitle()).
   
    driver: This is the object variable (e.g., in Python, Java, C#) that holds the reference to the actual browser session.
     When you write code like driver.get("http://www.google.com"), you are using this driver object to send commands to the web browser.
    
    run the testcase: pytest src/ex_01_seleniumBasics/test_selenium_01.py --alluredir allure-results
    
    allure report:   allure serve allure_results
    
    to activate the virtual environment: source .venv/bin/activate
    """

