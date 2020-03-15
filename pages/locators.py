from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, ".product_main p:nth-child(2)")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    MESSAGE_PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(1)")
    MESSAGE_BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert:nth-child(3)")
