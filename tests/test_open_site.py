from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MAIN_LOGIN_BUTTON


def test_open_stellar_burgers_main_login_button_visible(driver):
    """Главная страница открывается, кнопка 'Войти в аккаунт' видна."""
    main_login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MAIN_LOGIN_BUTTON)
    )
    assert main_login_button.is_displayed()