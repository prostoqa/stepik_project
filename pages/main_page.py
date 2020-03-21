from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def search_product(self, product_name):
        self.browser.find_element(*MainPageLocators.SEARCH_FIELD).send_keys(product_name)
        self.browser.find_element(*MainPageLocators.SEARCH_BUTTON).click()

    def select_books(self):
        self.browser.find_element(*MainPageLocators.BOOKS).click()

    def should_be_success_authorization(self):
        text_message = self.browser.find_element(*MainPageLocators.TEXT_MESSAGE).text
        assert self.is_element_present(*MainPageLocators.SUCCESS_MESSAGE), "Not success authorization"
        assert len(text_message) > 0, "No authorization message"
