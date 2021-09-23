import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    opt = Options()
    opt.add_experimental_option('prefs', {'intl.accept_languages': lang})

    if lang:
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=opt)
    else:
        raise pytest.UsageError("chose the --language")

    yield browser
    time.sleep(3)
    print("\nquit browser..")
    browser.quit()
