import time
import os
import math

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv

load_dotenv()


num = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]
result = ''


@pytest.mark.parametrize('num', num)
def test_links(browser, num):
    global result

    #     открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
    browser.get(f"https://stepik.org/lesson/{num}/step/1")

    #     авторизоваться со своими логином и паролем
    # browser.implicitly_wait(5)

    login_link = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "ember33")))
    print(login_link.text)
    login_link.click()

    # print(len(browser.window_handles))

    email = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    email_input = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.ID, "id_login_email")))
    email_input.send_keys(email)

    password_input = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.ID, "id_login_password")))
    password_input.send_keys(password)

    # print(browser.current_url)

    login_button = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='submit']")))
    login_button.click()

    print(browser.current_url)
    # print(login_button.get_attribute('style'))
    #     дождаться того, что поп-апа с авторизацией больше нет
    # modal_form = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog")))
    # print(modal_form)
    # assert login_button.get_attribute('style') == 'display: none;', "ew"

    try:
        again_button = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".again-btn.white")))
        print(again_button.text)
        again_button.click()

        alert_button = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-popup__container")))
        print(alert_button)
        confirm_button = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            ".modal-popup__container .data-ember-action.data-ember-action-34")))
        print(confirm_button, confirm_button.text)
        confirm_button.click()

    except:
        print("form is clear")
    time.sleep(10)

    textarea = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
    # print(textarea.text)
    answer = math.log(int(time.time()))
    textarea.send_keys(answer)

    # < textarea
    # id = "ember86"
    # class ="ember-text-area ember-view textarea string-quiz__textarea" style="height: 80px;" > < /textarea >

    answer_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    # print(answer_button.text)
    answer_button.click()

    correct_sign = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    print(correct_sign.text)
    if correct_sign.text != "Correct!":
        result += f" {correct_sign.text}"

    print(result)
