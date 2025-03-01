from asyncio import wait_for
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://stepik.org/lesson/236895/step/1'
browser = webdriver.Chrome()
browser.get(link)
WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]'))
    )
vhod = browser.find_element(By.CSS_SELECTOR, '[class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]')
vhod.click()
input_login = browser.find_element(
                   By.CSS_SELECTOR, '[autocomplete="email"]'
            )
input_login.send_keys("fortochkina.klawcka@yandex.ru")
input_pass = browser.find_element(
                   By.CSS_SELECTOR, '[autocomplete="password"]'
            )
input_pass.send_keys("2ab8o799Z")
button_send = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button_send.click()
answer = str(math.log(int(time.time())))
time.sleep(5)
text_area = browser.find_element(By.CSS_SELECTOR, '[class="ember-text-area ember-view textarea string-quiz__textarea"]')
text_area.send_keys(answer)
time.sleep(5)
button = browser.find_element(By.CSS_SELECTOR, '[class="submit-submission"]')
button.click()
time.sleep(100)
#message_element = WebDriverWait(driver, 10).until(
 #       EC.visibility_of_element_located((By.CLASS_NAME, "message"))
  #  )

    # Получение текста из элемента
  #  message_text = message_element.text

browser.quit()
