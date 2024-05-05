from .base_page import BasePage
from .locators import BasketPageLocators


class ProductPage(BasePage):

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*BasketPageLocators.ADD_TO_BASKET_BUTTON), "Btn add to basket is not presented"

    def add_product_to_basket(self):
        product_name = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text.split(" ")[0]
        btn = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET_BUTTON)
        btn.click()
        self.solve_quiz_and_get_code()
        alert_success = self.browser.find_elements(*BasketPageLocators.SUCCESS_ALERTS)[0]
        alert_info = self.browser.find_element(*BasketPageLocators.ALERT_INFO_BASKET_COUNT).text
        assert product_name in alert_success.text, f"Success alert not contains text about product:  {product_name}"
        assert product_price in alert_info, f"Success info not contains product's price: {product_name}/{product_price}"
