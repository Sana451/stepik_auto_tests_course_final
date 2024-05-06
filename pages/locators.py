from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button[value='Добавить в корзину']")
    SUCCESS_ALERT = (By.XPATH, "//strong[contains(text(),'Coders at Work')]")
    ALERT_INFO_BASKET_COUNT = (By.CLASS_NAME, "alert-info")

