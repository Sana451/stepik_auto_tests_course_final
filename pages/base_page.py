from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser: webdriver.Chrome, url: str, timeout: int = 5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by_how, what_element):
        try:
            self.browser.find_element(by_how, what_element)
            return True
        except NoSuchElementException:
            return False
