import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


def test_verify_actions_keyboard2():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # draggable click and hold
    draggable = driver.find_element(By.XPATH, "//div[@id='draggable']")
    actions_chain = ActionChains(driver)
    actions_chain.click_and_hold(draggable).perform()
    time.sleep(2)

    # Drag and drop
    droppable = driver.find_element(By.XPATH, "//div[@id='droppable']")
    actions_chain.drag_and_drop(draggable,droppable).perform()

    dropped =driver.find_element(By.XPATH, "//strong[@id='drop-status']")
    assert dropped.text == "dropped"
    time.sleep(2)
    driver.quit()