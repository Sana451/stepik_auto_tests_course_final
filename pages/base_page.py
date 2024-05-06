import math
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def is_not_element_present(self, by_how, what_element, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(
                    (by_how, what_element,)
                ))
            return False
        except TimeoutException:
            return True

    def is_disappeared(self, by_how, what_element, timeout=4):
        try:
            WebDriverWait(self, timeout).until_not(
                EC.presence_of_element_located(
                    (by_how, what_element,)
                ))
            return True
        except TimeoutException:
            return False

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
