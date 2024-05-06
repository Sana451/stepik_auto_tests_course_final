from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.LINK_TEXT, "Посмотреть корзину")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class CartPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[value='Добавить в корзину']")
    SUCCESS_ALERT = (By.XPATH, "//strong[contains(text(),'Coders at Work')]")
    ALERT_INFO_CART_COUNT = (By.CSS_SELECTOR, ".alert-info")
    PRODUCTS_IN_CART_TEXT = (By.XPATH, "//h2[contains(text(), 'Товары в корзине')]")
    PRODUCTS_IN_CART_COUNT = (By.XPATH, "//p[contains(text(), 'Количество')]")
    EMPTY_CART_TEXT = (By.XPATH, "//p[contains(text(), 'Ваша корзина пуста')]")
    CONTINUE_SHOPPING_LINK = (By.LINK_TEXT, "Продолжить покупки")
    GO_TO_PRODUCTS_REGISTRATION_LINK = (By.LINK_TEXT, "Перейти к оформлению")
