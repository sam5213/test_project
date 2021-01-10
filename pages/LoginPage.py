from selenium.webdriver.common.by import By

from config.config import TestData
from pages.BasePage import BasePage
from pages.HomePage import HomePage


class LoginPage(BasePage):

    LOGIN = (By.ID, "id_username")
    PASSWORD = (By.ID, "id_password")
    LOGIN_BUTTON = (By.ID, "auth_form_sub")
    SIGNUP_LINK = (By.LINK_TEXT, "Register")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_enabled(self.SIGNUP_LINK)

    def do_login(self, username, password):
        self.do_send_keys(self.LOGIN, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)
