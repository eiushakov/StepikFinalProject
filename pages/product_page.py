from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_product(self):
        product_name = self.take_product_name()
        product_cost = self.take_product_cost()
        self.press_to_add_button()
        self.solve_quiz_and_get_code()
        self.should_be_name_add_product(product_name)
        self.should_be_cost_add_product(product_cost)

    def take_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def take_product_cost(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        return product_cost

    def press_to_add_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_name_add_product(self, product_name):
        confirm_name = self.browser.find_element(*ProductPageLocators.PRODUCT_CONFIRM).text
        assert confirm_name == product_name, "Product is not added to cart"

    def should_be_cost_add_product(self, product_cost):
        cart_cost = self.browser.find_element(*ProductPageLocators.CART_COST).text
        assert cart_cost == product_cost, "Cost of cart is not match with product's cost"
