from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    MAIN_LOGIN_BUTTON,
    LOGIN_EMAIL_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_SUBMIT_BUTTON,
    MAKE_ORDER_BUTTON,
    PERSONAL_ACCOUNT_BUTTON,
    REGISTER_LINK,
    REGISTER_PAGE_LOGIN_LINK,
    FORGOT_PASSWORD_LINK,
    FORGOT_PASSWORD_EMAIL_INPUT,
    FORGOT_PASSWORD_SUBMIT_BUTTON,
    FORGOT_PASSWORD_PAGE_LOGIN_LINK,
)
from conftest import TEST_USER_EMAIL, TEST_USER_PASSWORD

def test_login_from_main_login_button(driver):
    # 1. Нажать "Войти в аккаунт" на главной
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    ).click()

    # 2. Заполнить форму логина
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
    ).send_keys(TEST_USER_EMAIL)

    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(TEST_USER_PASSWORD)

    # 3. Нажать "Войти"
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    # 4. Проверка: после успешного входа видим кнопку "Оформить заказ"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MAKE_ORDER_BUTTON)
    )

def test_login_from_personal_account_button(driver):
    # 1. Нажать "Личный кабинет" в шапке
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)
    ).click()

    # 2. Заполнить форму логина
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
    ).send_keys(TEST_USER_EMAIL)

    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(TEST_USER_PASSWORD)

    # 3. Нажать "Войти"
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    # 4. Проверка: после успешного входа видим кнопку "Оформить заказ"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MAKE_ORDER_BUTTON)
    )

def test_login_from_registration_form(driver):
    # 1. С главной перейти на форму регистрации
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(REGISTER_LINK)
    ).click()

    # 2. На странице регистрации нажать "Войти"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(REGISTER_PAGE_LOGIN_LINK)
    ).click()

    # 3. Заполнить форму логина
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
    ).send_keys(TEST_USER_EMAIL)

    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(TEST_USER_PASSWORD)

    # 4. Нажать "Войти"
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    # 5. Проверка: после успешного входа видим кнопку "Оформить заказ"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MAKE_ORDER_BUTTON)
    )    
def test_login_from_forgot_password_form(driver):
    # 1. С главной перейти на форму входа
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    ).click()

    # 2. Нажать "Восстановить пароль"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(FORGOT_PASSWORD_LINK)
    ).click()

    # 3. На странице восстановления нажать "Войти"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(FORGOT_PASSWORD_PAGE_LOGIN_LINK)
    ).click()

    # 4. Заполнить форму логина
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
    ).send_keys(TEST_USER_EMAIL)

    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(TEST_USER_PASSWORD)

    # 5. Нажать "Войти"
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    # 6. Проверка: после успешного входа видим кнопку "Оформить заказ"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MAKE_ORDER_BUTTON)
    )