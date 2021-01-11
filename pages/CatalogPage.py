from selenium.webdriver.common.by import By

from config import TestData
from pages.BasePage import BasePage


class CatalogPage(BasePage):

    UNIVERSITY = (By.ID, "filter_uni_chosen")
    COURSE_CATALOG = (By.LINK_TEXT, "Записаться на курсы")
    COURSE_LIST = (By.ID, "courses-found")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.HOME_PAGE_URL)

    def go_to_course_catalog(self):
        if self.is_enabled(self.COURSE_CATALOG):
            self.do_click(self.COURSE_CATALOG)

    def is_enabled_course_list(self):
        return self.is_enabled(self.COURSE_LIST)

    def is_enabled_uni_chosen(self):
        return self.is_enabled(self.UNIVERSITY)
