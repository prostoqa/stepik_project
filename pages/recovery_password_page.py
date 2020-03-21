from .base_page import BasePage
from .locators import RecoveryPageLocators


class RecoveryPage(BasePage):
    def password_reset(self, email):
        self.browser.find_element(*RecoveryPageLocators.RESET_EMAIL).send_keys(email)
        self.browser.find_element(*RecoveryPageLocators.RESET_BUTTON).click()

    def should_be_done_reset(self):
        assert "password-reset/done/" in self.browser.current_url, "Reset password failed"
