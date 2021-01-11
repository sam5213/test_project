from tests import BaseTest
from pages.CatalogPage import CatalogPage


class TestCatalogPage(BaseTest):

    def test_enabled_course_catalog(self, prepare_page):
        catalog_page = CatalogPage(self.driver)
        catalog_page.go_to_course_catalog()
        assert catalog_page.is_enabled_course_list()

    def test_enabled_uni_chosen(self, prepare_page):
        catalog_page = CatalogPage(self.driver)
        catalog_page.go_to_course_catalog()
        assert catalog_page.is_enabled_uni_chosen()
