from config.config import TestData
from pages.LoginPage import LoginPage
from tests.test_Base import BaseTest


class TestHomePage(BaseTest):

    def test_home_page_title(self):
        login_page = LoginPage(self.driver)
        home_page = login_page.do_login(TestData.LOGIN, TestData.PASSWORD)
        title = home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE
        login_page.do_logout()

    def test_home_page_slogan(self):
        login_page = LoginPage(self.driver)
        home_page = login_page.do_login(TestData.LOGIN, TestData.PASSWORD)
        slogan = home_page.get_slogan_value()
        assert slogan == TestData.SLOGAN
        login_page.do_logout()

