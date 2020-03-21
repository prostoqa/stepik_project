from .base_page import BasePage
from .locators import SearchPageLocators


class SearchPage(BasePage):
    def should_be_searching_product(self, product_name):
        assert product_name in self.browser.find_element(*SearchPageLocators.HEADER).text, "Wrong search"
        assert product_name == self.browser.find_element(*SearchPageLocators.SEARCH_RESULT).text, "No searching product"
