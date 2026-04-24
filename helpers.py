# helpers.py

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
    FORGOT_PASSWORD_PAGE_LOGIN_LINK,
    # регистрация
    NAME_INPUT,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    REGISTER_SUBMIT,
    REGISTER_ERROR_MESSAGE,
    # конструктор и личный кабинет
    BUNS_TAB,
    SAUCES_TAB,
    FILLINGS_TAB,
    ACTIVE_TAB,
    PROFILE_TAB,
    LOGOUT_BUTTON,
    CONSTRUCTOR_BUTTON,
    STELLAR_LOGO,
    LOGIN_HEADER,
)
from utils import TEST_USER_EMAIL, TEST_USER_PASSWORD


# ===== Хелперы для логина =====

def open_login_from_main(driver):
    """Открыть форму логина по кнопке 'Войти в аккаунт' на главной."""
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    ).click()


def open_login_from_personal_account_button(driver):
    """Открыть форму логина по кнопке 'Личный кабинет' в шапке."""
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)
    ).click()


def open_login_from_registration_page(driver):
    """Открыть форму логина через переход на страницу регистрации."""
    open_login_from_main(driver)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(REGISTER_LINK)
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(REGISTER_PAGE_LOGIN_LINK)
    ).click()


def open_login_from_forgot_password_page(driver):
    """Открыть форму логина через страницу восстановления пароля."""
    open_login_from_main(driver)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(FORGOT_PASSWORD_LINK)
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(FORGOT_PASSWORD_PAGE_LOGIN_LINK)
    ).click()


def fill_login_form_and_submit(driver):
    """Заполнить форму логина тестовым пользователем и отправить."""
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
    ).send_keys(TEST_USER_EMAIL)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(TEST_USER_PASSWORD)
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()


def assert_user_logged_in(driver):
    """Проверить, что пользователь залогинен: видна кнопка 'Оформить заказ'."""
    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MAKE_ORDER_BUTTON)
    ).is_displayed()


def login(driver):
    """Полный флоу логина: открыть форму, ввести данные, убедиться, что вошли."""
    open_login_from_main(driver)
    fill_login_form_and_submit(driver)
    assert_user_logged_in(driver)


def login_and_go_to_constructor(driver):
    """Авторизоваться и попасть в конструктор (главная страница после логина)."""
    login(driver)


# ===== Хелперы для регистрации =====

def open_registration_page(driver):
    """Открыть страницу регистрации через форму логина с главной."""
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(REGISTER_LINK)
    ).click()


def fill_registration_form(driver, name: str, email: str, password: str):
    """Заполнить форму регистрации заданными данными."""
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(NAME_INPUT)
    ).send_keys(name)
    driver.find_element(*EMAIL_INPUT).send_keys(email)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)


def submit_registration_form(driver):
    """Отправить форму регистрации."""
    driver.find_element(*REGISTER_SUBMIT).click()


def assert_on_login_page_after_registration(driver):
    """Проверить, что после регистрации открылась страница входа."""
    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_HEADER)
    ).is_displayed()


def assert_registration_error_message_visible(driver):
    """Проверить, что появилось сообщение об ошибке регистрации."""
    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(REGISTER_ERROR_MESSAGE)
    ).is_displayed()


# ===== Хелперы для конструктора =====

def go_to_sauces_tab(driver):
    """Перейти на вкладку 'Соусы' и дождаться её активации."""
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(SAUCES_TAB)
    ).click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(ACTIVE_TAB, "Соусы")
    )


def go_to_buns_tab(driver):
    """Перейти на вкладку 'Булки' и дождаться её активации."""
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(BUNS_TAB)
    ).click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(ACTIVE_TAB, "Булки")
    )


def go_to_fillings_tab(driver):
    """Перейти на вкладку 'Начинки' и дождаться её активации."""
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(FILLINGS_TAB)
    ).click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(ACTIVE_TAB, "Начинки")
    )


def get_active_tab_text(driver):
    """Вернуть текст активной вкладки конструктора."""
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ACTIVE_TAB)
    ).text


# ===== Хелперы для личного кабинета =====

def open_personal_account(driver):
    """Перейти в личный кабинет из шапки."""
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)
    ).click()


def assert_in_profile(driver):
    """Проверить, что мы в личном кабинете (вкладка 'Профиль')."""
    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PROFILE_TAB)
    ).is_displayed()


def go_to_constructor_from_personal_account_by_button(driver):
    """Вернуться в конструктор по кнопке 'Конструктор' в шапке."""
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(CONSTRUCTOR_BUTTON)
    ).click()


def go_to_constructor_from_personal_account_by_logo(driver):
    """Вернуться в конструктор по клику на логотип."""
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(STELLAR_LOGO)
    ).click()


def assert_in_constructor(driver):
    """Проверить, что мы в конструкторе (видим 'Оформить заказ')."""
    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MAKE_ORDER_BUTTON)
    ).is_displayed()


def logout(driver):
    """Выйти из аккаунта через личный кабинет."""
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LOGOUT_BUTTON)
    ).click()


def assert_on_login_page(driver):
    """Проверить, что мы на странице входа (заголовок 'Вход')."""
    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_HEADER)
    ).is_displayed()