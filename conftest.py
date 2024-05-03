import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_opts
from selenium.webdriver.firefox.options import Options as firefox_opts


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: 'chrome' or 'firefox'")
    parser.addoption("--language", action="store", default="en", help="Choose language: 'ru' or 'en'")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
        options = chrome_opts()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        fp = firefox_opts()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=fp)

    else:
        pytest.UsageError("--browser_name should be 'chrome' or 'firefox'")

    print(f"start test browser {browser_name} ...")
    yield browser
    print(f"quit test browser {browser_name} ...")
    browser.quit()
