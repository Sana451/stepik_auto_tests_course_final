import math
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser: webdriver.Chrome, url: str, timeout: int = 5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def go_to_login_cart_page(self):
        self.browser.find_element(*BasePageLocators.CART_LINK).click()

    def is_element_present(self, how, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
            return True
        except NoSuchElementException:
            return False

    def is_not_element_present(self, how, what: str, timeout: int = 4) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(
                    locator=(how, what,)
                ))
            return False
        except TimeoutException:
            return True

    def is_disappeared(self, how, what: str, timeout: int = 4) -> bool:
        try:
            WebDriverWait(self, timeout).until_not(
                EC.presence_of_element_located(
                    locator=(how, what,)
                ))
            return True
        except TimeoutException:
            return False

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), (
            "User icon is not presented, probably unauthorised user"
        )

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            time.sleep(10)
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
