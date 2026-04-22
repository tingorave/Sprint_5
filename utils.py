import random
import string


def generate_email():
    """Генерирует уникальный email в формате имя_фамилия_когорта_XXX@домен."""
    digits = "".join(random.choices(string.digits, k=3))
    return f"valentin_mikhanosha_5_{digits}@yandex.ru"


def generate_password(length: int = 8):
    """Генерирует случайный пароль нужной длины (буквы + цифры)."""
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choices(alphabet, k=length))