from selenium import webdriver
import pytest
import allure



def test_selenium_01():

    # Selenium 4

    driver =webdriver.Edge()
    driver.get("https://thetestingacademy.com")
    print (driver.title)
    assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"

    driver.quit()
