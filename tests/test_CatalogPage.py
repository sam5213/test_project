from config import TestData
from tests import BaseTest
from pages.LoginPage import LoginPage
from pages.CatalogPage import CatalogPage


class TestCatalogPage(BaseTest):

    def test_enabled_course_catalog(self):
        login_page = LoginPage(self.driver)
        login_page.do_login(TestData.LOGIN, TestData.PASSWORD)
        catalog_page = CatalogPage(self.driver)
        catalog_page.go_to_course_catalog()
        assert catalog_page.is_enabled_course_list()
        login_page.do_logout()

    def test_enabled_uni_chosen(self):
        login_page = LoginPage(self.driver)
        login_page.do_login(TestData.LOGIN, TestData.PASSWORD)
        catalog_page = CatalogPage(self.driver)
        catalog_page.go_to_course_catalog()
        assert catalog_page.is_enabled_uni_chosen()
        login_page.do_logout()
