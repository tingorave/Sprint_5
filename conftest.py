import pytest
from selenium import webdriver
from locators import BASE_URL

# Тестовый пользователь для входа
TEST_USER_EMAIL = "valentin_mikhanosha_sprint5@yandex.ru"
TEST_USER_PASSWORD = "Qwerty123"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()