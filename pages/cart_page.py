from pages.base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):

    def guest_cat_see_empty_cart_text(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_TEXT), (
            "Корзина не пустая (текст 'Ваша корзина пуста' отсутствует на странице корзины)")

    def guest_should_not_see_empty_cart_text(self):
        assert self.is_not_element_present(*CartPageLocators.EMPTY_CART_TEXT), (
            "Корзина пуста (на странице корзины присутствует текст 'Ваша корзина пуста')")

    def go_to_continue_shopping(self):
        self.browser.find_element(*CartPageLocators.CONTINUE_SHOPPING_LINK)

    def guest_can_see_products_in_cart_text_after_add(self):
        assert self.is_element_present(*CartPageLocators.PRODUCTS_IN_CART_TEXT), (
            "Текст 'Товары в корзине' отсутствует на странице корзины")

    def guest_can_see_products_in_cart_count_after_add(self):
        assert self.is_element_present(*CartPageLocators.PRODUCTS_IN_CART_COUNT), (
            "Текст 'Количество' отсутствует на странице корзины")

    def go_to_the_product_registration(self):
        self.browser.find_element(*CartPageLocators.GO_TO_PRODUCTS_REGISTRATION_LINK).click()
