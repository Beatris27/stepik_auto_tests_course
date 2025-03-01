from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK_REG = (By.CSS_SELECTOR, "#login_link")
    SIGNIN_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#register_form")