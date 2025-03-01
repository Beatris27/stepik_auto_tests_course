import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv

load_dotenv()


URL = "https://stepik.org/lesson/236895/step/1"


def test_login(browser):
    #     открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
    browser.get(URL)

    #     авторизоваться со своими логином и паролем
    browser.implicitly_wait(5)

    login_link = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "ember33")))
    print(login_link.text)
    # login_button = WebDriverWait(browser, 30).until(EC.visibility_of_element_located(By.ID, "ember33"))
    # login_button = browser.find_element(By.ID, "ember33")
    login_link.click()
    time.sleep(10)

    print(len(browser.window_handles))

    email = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    email_input = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.ID, "id_login_email")))
    print(email_input.text)
    email_input.send_keys(email)

    password_input = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.ID, "id_login_password")))
    print(password_input.text)
    password_input.send_keys(password)

    print(browser.current_url)

    login_button = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='submit']")))
    print(login_button.text)
    login_button.click()
    time.sleep(10)

    print(browser.current_url)
    # print(login_button.get_attribute('style'))
    #     дождаться того, что поп-апа с авторизацией больше нет
    # modal_form = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog")))
    # print(modal_form)
    # assert login_button.get_attribute('style') == 'display: none;', "ew"

