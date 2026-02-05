import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_verify_actions_keybord():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    # First name placeholder
    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    ActionChains(driver).key_down(Keys.SHIFT).send_keys_to_element(first_name, "santhoshi").key_up(Keys.SHIFT).perform()

    # Last name placeholder
    last_name = driver.find_element(By.XPATH, "//input[@name='lastname']")
    ActionChains(driver).key_down(Keys.SHIFT).send_keys_to_element(last_name, "kada").key_up(Keys.SHIFT).perform()

    time.sleep(2)
    driver.quit()


