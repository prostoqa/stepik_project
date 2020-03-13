from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def price_of_product(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def should_be_message_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), "No message that product added to basket"
        product_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_message == self.product_name(), "Wrong product name in message"

    def should_be_message_basket_total_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL_PRICE), "No message with total price"
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        assert price_message == self.price_of_product(), "Wrong total price in message"
