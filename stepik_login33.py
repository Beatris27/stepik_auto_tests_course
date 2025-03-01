import time
import math
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('link',
                         ["https://stepik.org/lesson/236895/step/1",
                          "https://stepik.org/lesson/236896/step/1",
                          "https://stepik.org/lesson/236897/step/1",
                          "https://stepik.org/lesson/236898/step/1",
                          "https://stepik.org/lesson/236899/step/1",
                          "https://stepik.org/lesson/236903/step/1",
                          "https://stepik.org/lesson/236904/step/1",
                          "https://stepik.org/lesson/236905/step/1"])

class Test8Urls:
    def test_login_link_stepik(self, browser, link):
        browser.get(link)
        button1 = browser.find_element(By.LINK_TEXT, "Войти")
        button1.click()
        input1 = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
        input1.send_keys("ya.n-bog@ya.ru")
        input2 = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
        input2.send_keys("30061988")
        button2 = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
        button2.click()
        time.sleep(5)
        element_selector = ".light-tabs.ember-view"
        elements = browser.find_elements(By.CSS_SELECTOR, element_selector)
        # Ассерт на невидимость окна авторизации
        assert len(elements) == 0, f"Элемент {element_selector} отображается на странице, хотя не должен."
        # Ввести ответ в поле и нажать кнопку
        input3 = browser.find_element(By.XPATH, "//textarea")
        # Ввод и Ожидание корректного ответа
        answer = str(math.log(int(time.time() + 0.3)))
        input3.send_keys(answer)
        button3 = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        button3.click()
        try:
            result_element = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
            result = result_element.text
            return "Correct!" in result
        except:
            result_element = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
            result = result_element.text
            print('Получено сообщение -', result)
            # button4 = browser.find_element(By.CSS_SELECTOR,".again-btn")
            # button4.click()
            return False
if __name__ == "__main__":
    pytest.main()