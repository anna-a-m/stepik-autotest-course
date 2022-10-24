from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calculate(x: str) -> float:
    x = int(x)
    result = math.log(abs(12*math.sin(x)))
    return result

LINK = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()

    x_value = browser.find_element(By.ID, "input_value")
    x_result = calculate(x_value.text)
    browser.find_element(By.ID, "answer").send_keys(x_result)
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()

finally:
    time.sleep(15)
    browser.quit()
