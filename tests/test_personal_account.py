from helpers import (
    login,
    open_personal_account,
    assert_in_profile,
    go_to_constructor_from_personal_account_by_button,
    go_to_constructor_from_personal_account_by_logo,
    assert_in_constructor,
    logout,
    assert_on_login_page,
)


def test_go_to_personal_account_from_header(driver):
    # 1. Залогиниться
    login(driver)

    # 2. Нажать "Личный кабинет" в шапке
    open_personal_account(driver)

    # 3. Проверка: мы в личном кабинете
    assert_in_profile(driver)


def test_go_to_constructor_from_personal_account_by_button(driver):
    # 1. Логин
    login(driver)

    # 2. Перейти в личный кабинет
    open_personal_account(driver)
    assert_in_profile(driver)

    # 3. Нажать "Конструктор" в шапке
    go_to_constructor_from_personal_account_by_button(driver)

    # 4. Проверка: вернулись в конструктор
    assert_in_constructor(driver)


def test_go_to_constructor_from_personal_account_by_logo(driver):
    # 1. Логин
    login(driver)

    # 2. Перейти в личный кабинет
    open_personal_account(driver)
    assert_in_profile(driver)

    # 3. Нажать на логотип Stellar Burgers
    go_to_constructor_from_personal_account_by_logo(driver)

    # 4. Проверка: вернулись в конструктор
    assert_in_constructor(driver)


def test_logout_from_personal_account(driver):
    # 1. Логин
    login(driver)

    # 2. Перейти в личный кабинет
    open_personal_account(driver)
    assert_in_profile(driver)

    # 3. Нажать "Выйти"
    logout(driver)

    # 4. Проверка: вернулись на страницу входа
    assert_on_login_page(driver)