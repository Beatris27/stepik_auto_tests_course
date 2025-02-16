from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID,"num1")
    x = x_element.text
    num1 = int(x)
    y_element = browser.find_element(By.ID,"num2")
    y = y_element.text
    num2 = int(y)
    sum_el = num1 + num2
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum_el))
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла