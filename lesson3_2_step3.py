from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest

class test(unittest.TestCase):

    # Ваш код, который заполняет обязательные поля
     def test1(self):
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)
            input_first_name = browser.find_element(
                   By.CSS_SELECTOR, '[placeholder="Input your first name"]'
            )
            input_first_name.send_keys("test")
            input_last_name = browser.find_element(
                   By.CSS_SELECTOR, '[placeholder="Input your last name"]'
            )
            input_last_name.send_keys("test")
            input_email = browser.find_element(
                   By.CSS_SELECTOR, '[placeholder="Input your email"]'
            )
            input_email.send_keys("test")
            input_phone = browser.find_element(
                   By.CSS_SELECTOR, '[placeholder="Input your phone:"]'
            )
            input_phone.send_keys("test")
            input_address = browser.find_element(
                   By.CSS_SELECTOR, '[placeholder="Input your address:"]'
            )
            input_address.send_keys("test")
            button_send = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
            button_send.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text: str = welcome_text_elt.text
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert("Congratulations! You have successfully registered!" == welcome_text)
            browser.quit()

     def test2(self):
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)
            input_first_name = browser.find_element(
                   By.CSS_SELECTOR, '[placeholder="Input your first name"]'
            )
            input_first_name.send_keys("test")
            input_last_name = browser.find_element(
                   By.CSS_SELECTOR, '[placeholder="Input your last name"]'
            )
            input_last_name.send_keys("test")
            input_email = browser.find_element(
                   By.CSS_SELECTOR, '[placeholder="Input your email"]'
            )
            input_email.send_keys("test")
            input_phone = browser.find_element(
                   By.CSS_SELECTOR, '[placeholder="Input your phone:"]'
            )
            input_phone.send_keys("test")
            input_address = browser.find_element(
                   By.CSS_SELECTOR, '[placeholder="Input your address:"]'
            )
            input_address.send_keys("test")
            button_send = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
            button_send.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert("Congratulations! You have successfully registered!" == welcome_text)
            browser.quit()

if __name__ == "__main__":
    unittest.main()


# не забываем оставить пустую строку в конце файла