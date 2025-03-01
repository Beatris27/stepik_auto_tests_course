from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.chrome.webdriver import WebDriver

link= "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_page_sigin_form(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    loginPage = LoginPage(browser, WebDriver.current_url)
    loginPage.should_be_login_form()  

def test_guest_should_see_login_in_url(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    loginPage = LoginPage(browser, WebDriver.current_url)
    loginPage.should_be_login_url() 

def test_guest_should_see_login_page_reg_form(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    loginPage = LoginPage(browser, WebDriver.current_url)
    loginPage.should_be_register_form()  