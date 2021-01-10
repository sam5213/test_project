from config.config import TestData
from pages.LoginPage import LoginPage
from tests.test_Base import BaseTest

class Test_Home(BaseTest):

    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.LOGIN, TestData.PASSWORD)
        title = homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_slogan(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.LOGIN, TestData.PASSWORD)
        slogan = homePage.get_slogan_value()
        assert slogan == TestData.SLOGAN

    def test_profile_icon(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.LOGIN, TestData.PASSWORD)
        assert homePage.is_setting_icon_exist()
