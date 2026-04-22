from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    MAIN_LOGIN_BUTTON,
    REGISTER_LINK,
    NAME_INPUT,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    REGISTER_SUBMIT,
    LOGIN_HEADER,
    REGISTER_ERROR_MESSAGE,
)
from utils import generate_email, generate_password


def test_success_registration(driver):
    # сгенерировать данные
    email = generate_email()
    password = generate_password(8)

    # 1. попасть на форму логина (на главной по кнопке "Войти в аккаунт")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    ).click()

    # 2. перейти на страницу регистрации
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(REGISTER_LINK)
    ).click()

    # 3. заполнить форму
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(NAME_INPUT)
    ).send_keys("Валентин")

    driver.find_element(*EMAIL_INPUT).send_keys(email)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)

    # 4. отправить
    driver.find_element(*REGISTER_SUBMIT).click()

      # 5. Проверка: после успешной регистрации оказались на форме входа
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_HEADER)
    )

def test_registration_incorrect_password(driver):
    # валидный email, но короткий пароль (меньше 6 символов)
    email = generate_email()
    short_password = "12345"

    # 1. попасть на форму логина
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    ).click()

    # 2. перейти на страницу регистрации
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(REGISTER_LINK)
    ).click()

    # 3. заполнить форму с некорректным паролем
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(NAME_INPUT)
    ).send_keys("Валентин")

    driver.find_element(*EMAIL_INPUT).send_keys(email)
    driver.find_element(*PASSWORD_INPUT).send_keys(short_password)

    # 4. отправить форму
    driver.find_element(*REGISTER_SUBMIT).click()

    # 5. Проверка: появилось сообщение об ошибке
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(REGISTER_ERROR_MESSAGE)
    )