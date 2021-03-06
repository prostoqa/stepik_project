from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.books_page import BooksPage
from .pages.recovery_password_page import RecoveryPage
from .pages.search_page import SearchPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/"
email = "mail213022@auto.test"
password = "Qwe123rty_"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                     # открываем страницу
        page.go_to_login_page()         # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_product_in_basket()
    page.should_be_empty_basket()


@pytest.mark.need_review_custom_scenarios
def test_guest_can_register(browser):
    new_mail = str(time.time()) + "@fakemail.org"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.register_new_user(new_mail, password)
    page = MainPage(browser, browser.current_url)
    page.should_be_success_authorization()
    page.should_be_authorized_user()


@pytest.mark.need_review_custom_scenarios
def test_user_can_log_in(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.user_log_in(email, password)
    page = MainPage(browser, browser.current_url)
    page.should_be_success_authorization()
    page.should_be_authorized_user()


@pytest.mark.need_review_custom_scenarios
def test_user_can_recovery_password(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.go_to_recovery_password()
    page = RecoveryPage(browser, browser.current_url)
    page.password_reset(email)
    page.should_be_done_reset()


class TestGuestSelectBookFromMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def select_product(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.select_books()
        page = BooksPage(browser, browser.current_url)
        self.book_name = page.get_book_name()

    @pytest.mark.need_review_custom_scenarios
    def test_guest_can_search_product(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.search_product(self.book_name)
        page = SearchPage(browser, browser.current_url)
        page.should_be_searching_product(self.book_name)

    @pytest.mark.need_review_custom_scenarios
    def test_guest_can_add_product_to_basket(self, browser):
        page = BooksPage(browser, browser.current_url)
        page.book_add_to_basket()
        page.should_be_message_product_added_to_basket_on_books_page(self.book_name)
        page.should_be_message_basket_total_price_on_books_page()
