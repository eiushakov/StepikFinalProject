import pytest
from .pages.product_page import ProductPage


@pytest.mark.xfail(reason="This is negative test, he don't be pass")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.press_to_add_button()
    page.guest_cant_see_success_message()


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message()


@pytest.mark.xfail(reason="This is negative test, he don't be pass")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.press_to_add_button()
    page.message_disappeared_after_adding_product_to_basket()
