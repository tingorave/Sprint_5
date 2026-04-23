from helpers import (
    login_and_go_to_constructor,
    go_to_sauces_tab,
    go_to_buns_tab,
    go_to_fillings_tab,
    get_active_tab_text,
)


def test_constructor_buns_tab(driver):
    # 1. Авторизуемся и попадаем в конструктор
    login_and_go_to_constructor(driver)

    # 2. Уходим с булок на соусы (чтобы потом проверить возврат)
    go_to_sauces_tab(driver)

    # 3. Возвращаемся на вкладку "Булки"
    go_to_buns_tab(driver)

    # 4. Проверяем, что активная вкладка — "Булки"
    assert get_active_tab_text(driver) == "Булки"


def test_constructor_sauces_tab(driver):
    # 1. Авторизуемся и попадаем в конструктор
    login_and_go_to_constructor(driver)

    # 2. Переходим на вкладку "Соусы"
    go_to_sauces_tab(driver)

    # 3. Проверяем, что активная вкладка — "Соусы"
    assert get_active_tab_text(driver) == "Соусы"


def test_constructor_fillings_tab(driver):
    # 1. Авторизуемся и попадаем в конструктор
    login_and_go_to_constructor(driver)

    # 2. Переходим на вкладку "Начинки"
    go_to_fillings_tab(driver)

    # 3. Проверяем, что активная вкладка — "Начинки"
    assert get_active_tab_text(driver) == "Начинки"