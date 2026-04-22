from locators import MAIN_LOGIN_BUTTON
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_stellar_burgers_main_login_button_visible(driver):
    # driver уже открыт на BASE_URL фикстурой из conftest.py
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MAIN_LOGIN_BUTTON)
    )