import time

import pytest

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.xfail(reason="Отрицательный тест")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.parametrize('offer_num',
                         [6,
                          [pytest.param(7, marks=pytest.mark.xfail(reason="some bug"))],
                          9])
def test_guest_can_add_product_to_basket(browser, offer_num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_btn()
    page.add_product_to_cart()


@pytest.mark.xfail(reason="Отрицательный тест")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.success_message_is_disappeared_after_add_to_cart()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    page.guest_cant_see_product_in_cart_opened_from_product_page()
    page.guest_can_see_product_empty_text_in_cart_opened_from_product_page()


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        print("TestUserAddToBasketFromProductPage started...")
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email="1@fakemail.org" + str(time.time()), password="password" + str(time.time()))
        login_page.should_be_authorized_user()
        yield
        print("TestUserAddToBasketFromProductPage finished...")

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_cart(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_cart_btn()
        page.add_product_to_cart()
