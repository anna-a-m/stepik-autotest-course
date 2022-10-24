from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


LINK = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    button.click()

finally:
    time.sleep(15)
    browser.quit()
