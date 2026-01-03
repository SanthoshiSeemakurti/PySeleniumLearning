from selenium import webdriver
import pytest
import allure



def test_selenium_01():

    # Selenium 4

    driver =webdriver.Firefox()
    driver.get("https://thetestingacademy.com")
    print (driver.title)
    print(driver.page_source )
    assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"

    driver.quit()
