from utils import generate_email, generate_password
from helpers import (
    open_registration_page,
    fill_registration_form,
    submit_registration_form,
    assert_on_login_page_after_registration,
    assert_registration_error_message_visible,
)


def test_success_registration(driver):
    # 0. Сгенерировать данные
    email = generate_email()
    password = generate_password(8)

    # 1. Открыть страницу регистрации
    open_registration_page(driver)

    # 2. Заполнить форму валидными данными
    fill_registration_form(driver, "Валентин", email, password)

    # 3. Отправить форму
    submit_registration_form(driver)

    # 4. Проверка: после успешной регистрации оказались на форме входа
    assert_on_login_page_after_registration(driver)


def test_registration_incorrect_password(driver):
    # 0. Валидный email, но короткий пароль (меньше 6 символов)
    email = generate_email()
    short_password = "12345"

    # 1. Открыть страницу регистрации
    open_registration_page(driver)

    # 2. Заполнить форму с некорректным паролем
    fill_registration_form(driver, "Валентин", email, short_password)

    # 3. Отправить форму
    submit_registration_form(driver)

    # 4. Проверка: появилось сообщение об ошибке
    assert_registration_error_message_visible(driver)