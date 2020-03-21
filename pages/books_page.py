from .base_page import BasePage
from .locators import BooksPageLocators


class BooksPage(BasePage):
    def book_add_to_basket(self):
        self.browser.find_element(*BooksPageLocators.ADD_TO_BASKET).click()

    def get_book_name(self):
        return self.browser.find_element(*BooksPageLocators.BOOK_NAME).text

    def get_book_price(self):
        return self.browser.find_element(*BooksPageLocators.BOOK_PRICE).text

    def should_be_message_product_added_to_basket_on_books_page(self, product_name):
        assert self.is_element_present(*BooksPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET_ON_BOOKS_PAGE), \
            "No message that product added to basket"
        product_name_in_message = self.browser.find_element(*BooksPageLocators.PRODUCT_NAME_IN_MESSAGE_ON_BOOKS_PAGE).text
        assert product_name_in_message == product_name, "Wrong product name in message"

    def should_be_message_basket_total_price_on_books_page(self):
        assert self.is_element_present(*BooksPageLocators.MESSAGE_BASKET_TOTAL_PRICE_ON_BOOKS_PAGE), \
            "No message with total price"
        price_in_message = self.browser.find_element(*BooksPageLocators.PRICE_IN_MESSAGE_ON_BOOKS_PAGE).text
        assert price_in_message == self.get_book_price(), "Wrong total price in message"
