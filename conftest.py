import pytest
from selenium import webdriver

from utils import BASE_URL, TEST_USER_EMAIL, TEST_USER_PASSWORD

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()