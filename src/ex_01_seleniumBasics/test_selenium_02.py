import pytest
import allure
from selenium import webdriver


def test_selenium_01():
    """
    # Selenium 3 - not much used
    driver_path ="/Users/shravankumarkada/Downloads/edgedriver_mac64_m1/msedgedriver"
    driver = webdriver.EdgeService(executable_path=driver_path)
    above 2 lines are optional in selenium 4
    """
    driver =webdriver.Edge()
    driver.get("https://thetestingacademy.com")
    print (driver.title)
    assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"

    driver.quit()
