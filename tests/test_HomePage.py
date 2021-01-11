from config.config import TestData
from tests.test_Base import BaseTest


class TestHomePage(BaseTest):

    def test_home_page_title(self, prepare_page):
        home_page = prepare_page
        title = home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_slogan(self, prepare_page):
        home_page = prepare_page
        slogan = home_page.get_slogan_value()
        assert slogan == TestData.SLOGAN

