"""
#  Navigate to the MakeMyTrip.com
# use action class to enter the flight from New Delhi(DEL) to Chandigarh(IXC).
"""
# Actions: Action class is an ability provided by Selenium for handling key bord and mouse events

import time

import allure

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@allure.title("Make My Trip login Positive Testcase")
@allure.description(" Verify 'enter the flight from Delhi to Chandigarh'")

def test_make_my_trip_flight_from_Delhi():
    driver = webdriver.Chrome()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver.get("https://www.makemytrip.com/")
    time.sleep(2)

    # actions reference and object creation
    actions = ActionChains(driver)

    # minimize AI chat bot window
    """
    <img 
        alt="minimize" 
        src="https://jsak.mmtcdn.com/pwa/platform-myra-ui/static/sub_icons/close-icon.png">
    """
    # element_ai_chat_bot_window = driver.find_element(By.XPATH, "//img[@alt='minimize']")
    # element_ai_chat_bot_window.click()

    # close Modal
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='commonModal__close']")))
    element_modal_close = driver.find_element(By.XPATH, "//span[@class='commonModal__close']")
    element_modal_close.click()

    # From city
    from_city_place_holder = driver.find_element(By.XPATH, "//input[@id='fromCity']")
    # actions. = ActionChains
    from_city_place_holder.click()
    time.sleep(2)

    # To City
    """
    <input 
    data-cy="toCity" 
    id="toCity" 
    class="fsw_inputField 
    lineHeight36 latoBlack font30" 
    readonly="" 
    type="text" 
    value="Bengaluru">
    """
    to_city_place_holder= driver.find_element(By.XPATH, "//input[@id='toCity']")
    to_city_place_holder.send_keys("IXC")


    time.sleep(6)

    driver.quit()


















