from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        text_in_basket = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert "Your basket is empty." in text_in_basket, "Basket not empty"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "There is a product in the basket"
