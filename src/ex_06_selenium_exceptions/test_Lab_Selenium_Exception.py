import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@allure.title("Exception handling")
@allure.testcase()
@allure.description("Verify exception_handling")
def test_exception_handle():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    try:
        element= driver.find_element(By.XPATH, "//input[@id='No Such ID']")
        element.send_keys("Saran.mitra@gmail.com")
        time.sleep(2)
    except NoSuchElementException as nse:
        print(nse.msg)

    driver.quit()
