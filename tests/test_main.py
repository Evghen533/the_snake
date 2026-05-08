import pytest


def add_sum(a, b):
    """Возвращает сумму двух чисел."""
    return a + b


@pytest.mark.smoke
def test_add():
    """Тест сложения (smoke)."""
    assert add_sum(2, 3) == 5, 'сумма не равна ожидаемой'


@pytest.mark.parametrize('x, y, expected', [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_addition(x, y, expected):
    """Параметризованный тест сложения."""
    assert x + y == expected


def test_addition_with_fixture(sample_numbers):
    """Тест с использованием фикстуры sample_numbers."""
    # Шаг 1: Проверка доступности (отладка)
    print(f"\nDebug sample_numbers: {sample_numbers}")
    a, b, expected = sample_numbers
    assert a + b == expected, f'{a} + {b} должно быть {expected}'


def test_data_processing(temporary_data):
    """Проверка обработки временных данных."""
    # Шаг 1: Проверка доступности (отладка)
    print(f"\nDebug temporary_data: {temporary_data}")
    assert sum(temporary_data) == 15
    assert len(temporary_data) == 5
