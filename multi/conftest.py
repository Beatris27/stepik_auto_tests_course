import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



#def pytest_addoption(parser):
#    parser.addoption('--language', action='store', default=None,
#                     help="Choose language: en, rus, fr etc.")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()