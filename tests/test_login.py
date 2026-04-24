from helpers import (
    open_login_from_main,
    open_login_from_personal_account_button,
    open_login_from_registration_page,
    open_login_from_forgot_password_page,
    fill_login_form_and_submit,
    assert_user_logged_in,
)


def test_login_from_main_login_button(driver):
    # 1. Открыть форму логина с главной
    open_login_from_main(driver)
    # 2. Заполнить форму и отправить
    fill_login_form_and_submit(driver)
    # 3. Проверка: пользователь залогинен
    assert_user_logged_in(driver)


def test_login_from_personal_account_button(driver):
    # 1. Открыть форму логина по кнопке "Личный кабинет"
    open_login_from_personal_account_button(driver)
    # 2. Заполнить форму и отправить
    fill_login_form_and_submit(driver)
    # 3. Проверка: пользователь залогинен
    assert_user_logged_in(driver)


def test_login_from_registration_form(driver):
    # 1. Открыть форму логина через страницу регистрации
    open_login_from_registration_page(driver)
    # 2. Заполнить форму и отправить
    fill_login_form_and_submit(driver)
    # 3. Проверка: пользователь залогинен
    assert_user_logged_in(driver)


def test_login_from_forgot_password_form(driver):
    # 1. Открыть форму логина через страницу восстановления пароля
    open_login_from_forgot_password_page(driver)
    # 2. Заполнить форму и отправить
    fill_login_form_and_submit(driver)
    # 3. Проверка: пользователь залогинен
    assert_user_logged_in(driver)