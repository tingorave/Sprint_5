from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    MAIN_LOGIN_BUTTON,
    LOGIN_EMAIL_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_SUBMIT_BUTTON,
    MAKE_ORDER_BUTTON,
    BUNS_TAB,
    SAUCES_TAB,
    FILLINGS_TAB,
    ACTIVE_TAB,
)
from conftest import TEST_USER_EMAIL, TEST_USER_PASSWORD

def login_and_go_to_constructor(driver):
    # вспомогательная функция внутри файла, не тест
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
    ).send_keys(TEST_USER_EMAIL)

    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(TEST_USER_PASSWORD)
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MAKE_ORDER_BUTTON)
    )


def test_constructor_buns_tab(driver):
    # Просто зайти в конструктор (булки должны быть активны по умолчанию)
    login_and_go_to_constructor(driver)

    active_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ACTIVE_TAB)
    ).text

    assert active_text == "Булки"


def test_constructor_sauces_tab(driver):
    login_and_go_to_constructor(driver)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(SAUCES_TAB)
    ).click()

    active_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ACTIVE_TAB)
    ).text

    assert active_text == "Соусы"


def test_constructor_fillings_tab(driver):
    login_and_go_to_constructor(driver)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(FILLINGS_TAB)
    ).click()

    active_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ACTIVE_TAB)
    ).text

    assert active_text == "Начинки"