import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# Список ссылок на тестируемые страницы
links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.fixture(scope='function')
def answer():
    """Фикстура, возвращающая результат формулы math.log(int(time.time()))."""
    return str(math.log(int(time.time())))


class TestStepik:
    @classmethod
    def setup_class(cls):
        """Инициализация веб-драйвера и установка неявного ожидания."""
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(5)

    @classmethod
    def teardown_class(cls):
        """Закрытие браузера после выполнения всех тестов."""
        cls.browser.quit()

    @pytest.mark.parametrize('link', links)
    def test_stepik(self, link, answer):
        # Открываем страницу
        self.browser.get(link)

        # Ждем появления кнопки "Войти" и выполняем вход
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]'))
        )
        login_button = self.browser.find_element(
            By.CSS_SELECTOR, '[class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]'
        )
        login_button.click()

        # Вводим логин и пароль
        email_input = self.browser.find_element(By.CSS_SELECTOR, '[autocomplete="email"]')
        email_input.send_keys("fortochkina.klawcka@yandex.ru")

        password_input = self.browser.find_element(By.CSS_SELECTOR, '[autocomplete="password"]')
        password_input.send_keys("2ab8o799Z")
        time.sleep(5)

        # Нажимаем кнопку отправки формы
        submit_button = self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
        submit_button.click()
        time.sleep(5)
        # Ожидаем появления поля для ввода ответа
        textarea = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
        )

        # Вводим ответ
        textarea.send_keys(answer)

        # Нажимаем кнопку "Отправить"
        submit_button = self.browser.find_element(By.CSS_SELECTOR, "[class='submit-submission']")
        submit_button.click()
        time.sleep(15)

        # Ожидаем появления фидбека
        feedback = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'pre.smart-hints__hint'))
        ).text

        # Проверяем, что фидбек равен "Correct!"
        assert feedback == "Correct!", f"Ожидался текст 'Correct!', но получен '{feedback}'"

