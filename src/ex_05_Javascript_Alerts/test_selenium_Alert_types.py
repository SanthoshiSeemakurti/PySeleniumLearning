"""
Explore types of Alerts:
Navigate to "https://the-internet.herokuapp.com/javascript_alerts"
"""
from ftplib import all_errors

import allure
import pytest
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_javascript_alerts_prompt():
    driver= webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # JS alert:
    """<button onclick="jsAlert()">Click for JS Alert</button>"""

    element_jsAlert = driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Alert')]")
    element_jsAlert.click()

    WebDriverWait(driver, timeout=3).until(EC.alert_is_present())
    time.sleep(2)

    alert = driver.switch_to.alert
    alert.accept()

    time.sleep(2)
    """
    <p id="result" style="color:green">You successfully clicked an alert</p>
    """
    result_text= driver.find_element(By.XPATH, "//p[contains(text(),'You successfully clicked an alert')]").text
    assert result_text == "You successfully clicked an alert"

    driver.quit()


def test_alert_confirm():
    driver = webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # JS alert:

    """<button 
    onclick="jsConfirm()">Click for JS Confirm</button>
    """
    element_js_confirm = driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
    element_js_confirm.click()

    time.sleep(2)

    alert = driver.switch_to.alert
    alert.dismiss()

    """<p id="result" style="color:green">You clicked: Cancel</p>
    """
    result_text2 ="You clicked: Cancel"
    assert result_text2 == "You clicked: Cancel"

    driver.quit()

def test_alert_js_prompt():
    driver= webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # JS alert:

    """<button onclick="jsPrompt()">Click for JS Prompt</button>"""
    element_js_prompt = driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Prompt')]")
    element_js_prompt.click()

    time.sleep(2)
    alert = driver.switch_to.alert
    alert.send_keys("ZARA")
    alert.accept()

    time.sleep(2)

    """<p id="result" style="color:green">You entered: zara</p>"""
    result_text= driver.find_element(By.ID, "result").text
    assert result_text == "You entered: ZARA"

    driver.quit()