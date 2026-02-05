import time
import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Exception handling")
@allure.description("Verify Time out exception")
def test_time_out_exceptions():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        WebDriverWait(driver= driver,timeout= 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='submit']")))
        print("End of the Program")
    except TimeoutException as toe:
        print(toe.msg)
        print("Time out exception occurred!!")
    driver.quit()