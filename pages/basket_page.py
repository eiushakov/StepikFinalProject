from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.guest_cant_see_product_in_basket()
        self.guest_can_see_text_about_empty_basket()

    def should_be_basket_url(self):
        current_link = self.browser.current_url
        assert current_link.find("basket") != -1, "Substring 'basket' is not in URL of the current page"

    def guest_cant_see_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "Product in basket is presented, " \
                                                                                    "but should not be "

    def guest_can_see_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), 'Text "Your basket is empty" is not ' \
                                                                              'presented '
