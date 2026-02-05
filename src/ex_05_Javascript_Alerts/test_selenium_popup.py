import allure
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@allure.title("Make My Trip login Positive Testcase")
@allure.description(" Verify 'enter the flight from Delhi to Chandigarh'")
def test_selenium_popup():


    driver = webdriver.Chrome()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver.get("https://www.makemytrip.com/")


    # close Modal
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='commonModal__close']")))

    element_modal_close = driver.find_element(By.XPATH, "//span[@class='commonModal__close']")
    element_modal_close.click()

    time.sleep(2)
    driver.quit()

