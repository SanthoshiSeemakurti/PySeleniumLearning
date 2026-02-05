import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Task 2: 
    Click on a Specific State (Example: Maharashtra)
        URL :- https://www.amcharts.com/svg-maps/?map=india
    Locate Maharashtra using SVG path
    Click on Maharashtra
    Validate:
    Tooltip OR State name is displayed OR
    Any visual highlight happens
"""

@allure.title("SVG")
@allure.description("verifySVG")
def test_svg_amcharts():
    driver = webdriver.Chrome()


    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    # svg: we use name() or local-name() in xpath

    states= driver.find_elements(By.XPATH,"//*[name()= 'svg']//*[name()= 'path' and @aria-label]")
    for state in states:
        print(state.get_attribute("aria-label"))
        if "Maharashtra" in state.get_attribute("aria-label"):
            driver.execute_script("""
                arguments[0].dispatchEvent(
                    new MouseEvent('click', {
                        bubbles: true,
                        cancelable: true,
                        view: window
                    })
                );
            """, state)

            time.sleep(1)

            #state name verification
            tooltip = state.get_attribute("aria-label")
            assert "Maharashtra" in tooltip
            print("Tooltip verified", tooltip)
            time.sleep(3)

            # Verify fill colour
            fill_color = state.get_attribute("fill")
            print("Fill color after click:", fill_color)

            assert fill_color == "#FFFFFF"

            break


    time.sleep(1)
    driver.quit()

"""
Interview one-liner 🧑‍💼💡
    “SVG elements require name() or local-name() in XPath because they belong to a different XML namespace, and 
    map regions are usually represented as <path> elements with identifiable attributes like aria-label.”
🧠 One-liner to remember forever
    HTML elements can be clicked.
    SVG elements must receive mouse events.
"""

