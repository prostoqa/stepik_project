from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")


class BooksPageLocators:
    BOOK_NAME = (By.CSS_SELECTOR, "section .row li:nth-child(3) [title]")
    ADD_TO_BASKET = (By.CSS_SELECTOR, "section .row li:nth-child(3) button")
    BOOK_PRICE = (By.CSS_SELECTOR, "section .row li:nth-child(3) .price_color")
    PRODUCT_NAME_IN_MESSAGE_ON_BOOKS_PAGE = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PRICE_IN_MESSAGE_ON_BOOKS_PAGE = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    MESSAGE_PRODUCT_ADDED_TO_BASKET_ON_BOOKS_PAGE = (By.CSS_SELECTOR, ".alert:nth-child(1)")
    MESSAGE_BASKET_TOTAL_PRICE_ON_BOOKS_PAGE = (By.CSS_SELECTOR, ".alert:nth-child(3)")


class MainPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".icon-ok-sign")
    TEXT_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    BOOKS = (By.CSS_SELECTOR, ".dropdown-submenu")
    SEARCH_FIELD = (By.CSS_SELECTOR, "#id_q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".collapse [method='get'] .btn")


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[name='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    RECOVERY_LINK = (By.CSS_SELECTOR, "#login_form a")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, ".product_main p:nth-child(2)")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    MESSAGE_PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(1)")
    MESSAGE_BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert:nth-child(3)")


class RecoveryPageLocators:
    RESET_EMAIL = (By.CSS_SELECTOR, "#id_email")
    RESET_BUTTON = (By.CSS_SELECTOR, ".btn-lg")


class SearchPageLocators:
    HEADER = (By.CSS_SELECTOR, ".page-header h1")
    SEARCH_RESULT = (By.CSS_SELECTOR, "section .row li [title]")
