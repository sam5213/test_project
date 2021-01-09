import pytest
from selenium import webdriver

from config import TestData

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXUTABLE_PATH)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()
