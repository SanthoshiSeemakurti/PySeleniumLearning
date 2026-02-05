import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@allure.title("Select dropdown")
@allure.description("verify dropdown")
@allure.severity(allure.severity_level.NORMAL)

def test_svg_amcharts():
    driver = webdriver.Chrome()

    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    select_html_tag =driver.find_element(By.ID, "map")
    select = Select(select_html_tag)
    select.select_by_visible_text("Germany")
    time.sleep(3)
    driver.quit()
    

