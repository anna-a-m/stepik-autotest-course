from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

LINK = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    el_1 = browser.find_element(By.ID, "num1").text
    el_2 = browser.find_element(By.ID, "num2").text
    el_sum = int(el_1) + int(el_2)
    x_element = browser.find_element(By.CSS_SELECTOR,
                                     f"#dropdown option[value=\"{el_sum}\"]")
    x_element.click()

    browser.find_element(By.CSS_SELECTOR, "button[type=\"Submit\"]").click()

finally:
    time.sleep(15)
    browser.quit()
