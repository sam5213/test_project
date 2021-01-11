from config.config import TestData
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    SLOGAN = (By.XPATH, "//div[2]//div//h1")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.HOME_PAGE_URL)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def get_slogan_value(self):
        if self.is_enabled(self.SLOGAN):
            return self.get_element_text(self.SLOGAN)

