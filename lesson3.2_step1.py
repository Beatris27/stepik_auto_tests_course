from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"Ошибка: ожидалось '{expected_result}', но получено '{actual_result}'"

# Пример использования функции
try:
    test_input_text("Hello, World!", "Hello, world!")
except AssertionError as e:
    print(e)  # Выводит: Ошибка: ожидалось 'Hello, World!', но получено 'Hello, world!'