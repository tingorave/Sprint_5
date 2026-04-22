from selenium.webdriver.common.by import By

# Базовый адрес сайта
BASE_URL = "https://stellarburgers.education-services.ru/"

# Кнопка "Войти в аккаунт" на главной
MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

# --- Регистрация ---
REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")  # ссылка "Зарегистрироваться" под формой логина
NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # поле Имя
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # поле Email
PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # поле Пароль
REGISTER_SUBMIT = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка отправки формы регистрации

# Ссылка "Войти" на странице регистрации
REGISTER_PAGE_LOGIN_LINK = (By.LINK_TEXT, "Войти")

# Страница входа
LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")  # заголовок формы входа

# Поля формы входа
LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
LOGIN_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Ссылка "Восстановить пароль" на форме входа
FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")

# Поле Email на странице восстановления пароля
FORGOT_PASSWORD_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")

# Кнопка "Восстановить" на странице восстановления
FORGOT_PASSWORD_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

# Ссылка "Войти" на странице восстановления пароля
FORGOT_PASSWORD_PAGE_LOGIN_LINK = (By.LINK_TEXT, "Войти")

# Кнопка "Конструктор" в шапке
CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор")

# Логотип Stellar Burgers в шапке
STELLAR_LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]")

# Вкладка/ссылка "Профиль" в личном кабинете
PROFILE_TAB = (By.LINK_TEXT, "Профиль")

# Кнопка "Личный кабинет" в шапке
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

# Кнопка "Выход" в личном кабинете
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

# То, что увидим после успешного входа/регистрации
MAKE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")  # кнопка на главной для авторизованного юзера

# Сообщение об ошибке некорректного пароля при регистрации
REGISTER_ERROR_MESSAGE = (By.XPATH, "//*[contains(text(),'Некорректный пароль')]")

# --- Конструктор: вкладки ---
BUNS_TAB = (By.XPATH, "//span[text()='Булки']/..")
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/..")
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/..")

# Активная вкладка конструктора
ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span")