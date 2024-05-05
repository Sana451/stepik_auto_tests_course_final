import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize('offer_num',
                         [num for num in range(6, 9) if (num != 7)] +
                         [pytest.param(7, marks=pytest.mark.xfail(reason="some bug"))]
                         )
def test_guest_can_add_product_to_basket(browser, offer_num):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer{offer_num}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_product_to_basket()
