from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    MAIN_LOGIN_BUTTON,
    LOGIN_EMAIL_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_SUBMIT_BUTTON,
    MAKE_ORDER_BUTTON,
    PERSONAL_ACCOUNT_BUTTON,
    PROFILE_TAB,
    CONSTRUCTOR_BUTTON,
    STELLAR_LOGO,
    LOGOUT_BUTTON,
    LOGIN_HEADER,
)
from conftest import TEST_USER_EMAIL, TEST_USER_PASSWORD


def test_go_to_personal_account_from_header(driver):
    # 1. Сначала залогиниться (через кнопку "Войти в аккаунт" на главной)
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

    # 2. Нажать "Личный кабинет" в шапке
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)
    ).click()

    # 3. Проверка: мы в личном кабинете (видим вкладку/заголовок "Профиль")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PROFILE_TAB)
    )

def test_go_to_constructor_from_personal_account_by_button(driver):
    # 1. Логин
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

    # 2. Перейти в личный кабинет
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PROFILE_TAB)
    )

    # 3. Нажать "Конструктор" в шапке
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(CONSTRUCTOR_BUTTON)
    ).click()

    # 4. Проверка: вернулись в конструктор (например, видим кнопку "Оформить заказ")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MAKE_ORDER_BUTTON)
    )    

def test_go_to_constructor_from_personal_account_by_logo(driver):
    # 1. Логин
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

    # 2. Перейти в личный кабинет
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PROFILE_TAB)
    )

    # 3. Нажать на логотип Stellar Burgers
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(STELLAR_LOGO)
    ).click()

    # 4. Проверка: вернулись в конструктор (видим "Оформить заказ")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MAKE_ORDER_BUTTON)
    )    

def test_logout_from_personal_account(driver):
    # 1. Логин
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

    # 2. Перейти в личный кабинет
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PROFILE_TAB)
    )

    # 3. Нажать "Выйти"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LOGOUT_BUTTON)
    ).click()

    # 4. Проверка: вернулись на страницу входа (видим заголовок "Вход")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_HEADER)
    )