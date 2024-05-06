from .base_page import BasePage
from .locators import BasketPageLocators


class ProductPage(BasePage):

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*BasketPageLocators.ADD_TO_BASKET_BUTTON), "Btn add to basket is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *BasketPageLocators.SUCCESS_ALERT), "Success message is presented, but should not be"

    def add_product_to_basket(self):
        btn = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET_BUTTON)
        btn.click()
        self.solve_quiz_and_get_code()
        product_name = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text.split(" ")[0]
        success_add_basket_msg = self.browser.find_element(*BasketPageLocators.SUCCESS_ALERT)
        alert_info = self.browser.find_element(*BasketPageLocators.ALERT_INFO_BASKET_COUNT).text
        assert product_name == success_add_basket_msg.text, \
            f"Success alert not contains text about product: {product_name}"
        assert product_price in alert_info, f"Success info not contains product's price: {product_name}/{product_price}"

    def success_message_is_disappeared_after_add_to_basket(self):
        assert self.is_disappeared(*BasketPageLocators.SUCCESS_ALERT)

