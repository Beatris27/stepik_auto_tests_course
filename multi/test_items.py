from selenium.webdriver.common.by import By
import time


def test_guest_should_see_add_to_cart_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30) #задержка для оценки страницы вручную, можно закомментить для более быстрой проверки работоспособности теста
    button_buy = browser.find_elements(By.XPATH, "//button[contains(@class, 'add-to-basket')]")
    assert len(button_buy) > 0, "Не нашёл кнопку"