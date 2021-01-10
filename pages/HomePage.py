from config.config import TestData
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.HOME_PAGE_URL)

    SLOGAN = (By.XPATH, "//div[2]//div//h1")
    PROFILE_TEXT = (By.CSS_SELECTOR, "dropdown-login__text")
    PROFILE_ICON = (By.XPATH, "//div//span//span[1]")

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_setting_icon_exist(self):
        return self.is_enabled(self.PROFILE_ICON)

    def get_slogan_value(self):
        if self.is_enabled(self.SLOGAN):
            return self.get_element_text(self.SLOGAN)

    def get_profile_text_value(self):
        if self.is_enabled(self.PROFILE_TEXT):
            return self.get_element_text(self.PROFILE_TEXT)
