import pytest


@pytest.fixture
def sample_numbers():
    """Возвращает кортеж из двух чисел и их суммы для теста сложения."""
    return 2, 3, 5


@pytest.fixture(scope='session')
def temporary_data():
    """Возвращает список чисел.

    Использует область видимости 'session', чтобы список был общим
    для всех тестов в рамках одного запуска.
    """
    return [1, 2, 3, 4, 5]
