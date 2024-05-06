from .base_page import BasePage
from .locators import BasePageLocators, MainPageLocators, CartPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCTS_IN_CART_TEXT)

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.CART_LINK)
        link.click()

    def guest_can_see_product_empty_text_in_basket_opened_from_main_page(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_TEXT)
