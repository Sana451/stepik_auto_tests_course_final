from .base_page import BasePage
from .locators import CartPageLocators, BasePageLocators


class ProductPage(BasePage):

    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*CartPageLocators.ADD_TO_CART_BUTTON), "Btn add to basket is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *CartPageLocators.SUCCESS_ALERT), "Success message is presented, but should not be"

    def add_product_to_cart(self):
        btn = self.browser.find_element(*CartPageLocators.ADD_TO_CART_BUTTON)
        btn.click()
        self.solve_quiz_and_get_code()
        product_name = self.browser.find_element(*CartPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*CartPageLocators.PRODUCT_PRICE).text.split(" ")[0]
        success_add_cart_msg = self.browser.find_element(*CartPageLocators.SUCCESS_ALERT)
        alert_info = self.browser.find_element(*CartPageLocators.ALERT_INFO_CART_COUNT).text
        assert product_name == success_add_cart_msg.text, \
            f"Success alert not contains text about product: {product_name}"
        assert product_price in alert_info, f"Success info not contains product's price: {product_name}/{product_price}"

    def success_message_is_disappeared_after_add_to_cart(self):
        assert self.is_disappeared(*CartPageLocators.SUCCESS_ALERT)

    def should_not_be_products_in_cart(self):
        assert self.is_not_element_present(
            *CartPageLocators.PRODUCTS_IN_CART_TEXT
        ), "Корзина не пуста (title 'Products in cart is not presented')"

    def go_to_cart_page(self):
        link = self.browser.find_element(*BasePageLocators.CART_LINK)
        link.click()

    def guest_cant_see_product_in_cart_opened_from_product_page(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCTS_IN_CART_TEXT), (
            "На странице есть сведения о наличии в товаров в корзине, которых быть там не должно")

    def guest_can_see_product_empty_text_in_cart_opened_from_product_page(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_TEXT), (
            "Отсутствует текст 'корзина пуста' хотя подразумевается, что она пуста")
