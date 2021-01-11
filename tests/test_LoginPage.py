from config.config import TestData
from pages.LoginPage import LoginPage
from tests.test_Base import BaseTest


class TestLoginPage(BaseTest):

    def test_signup_link_visible(self):
        login_page = LoginPage(self.driver)
        assert login_page.is_signup_link_exist()

    def test_login_page_title(self):
        login_page = LoginPage(self.driver)
        title = login_page.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.do_login(TestData.LOGIN, TestData.PASSWORD)
        assert login_page.is_profile_icon_exist()

