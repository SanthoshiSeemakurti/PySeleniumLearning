from selenium import webdriver
import pytest
import allure


@allure.title("Print the Page source of the page ")
def test_selenium_01():

    # Selenium 4

    driver =webdriver.Firefox()
    driver.get("https://thetestingacademy.com")
    print (driver.title)
    print(driver.page_source )
    assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"

    driver.quit()


"""
    **To See the Allure Report**
    so if you want to run a pytest with HTML allure report to generate the HTML report,
        pytest src/ex_02_seleniumCommands/test_selenium_06_All_Browsers.py --alluredir allure-results

    ** this is a command to see the results of nLiver **
        allure serve allure-results/
    """