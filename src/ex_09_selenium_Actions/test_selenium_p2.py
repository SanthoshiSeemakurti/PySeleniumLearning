import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


def test_verify_actions_keyboard2():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # Navigate to front and back page
    # front page
    front_page = driver.find_element(By.XPATH, "//a[@id='click']")
    front_page.click()

    # result page
    result_page = driver.find_element(By.XPATH, "//p[@id='greeting']")
    assert result_page.text == "Success!"
    time.sleep(2)

    actions_builder = ActionBuilder(driver)
    actions_builder.pointer_action.pointer_up(MouseButton.BACK)
    actions_builder.perform()

    time.sleep(2)
    driver.quit()