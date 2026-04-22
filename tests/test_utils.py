from utils import generate_email, generate_password


def test_generate_email_format():
    email = generate_email()
    assert "@yandex.ru" in email
    assert len(email) > 10


def test_generate_password_length():
    password = generate_password(10)
    assert len(password) == 10