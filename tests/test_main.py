import pytest


def add_sum(a, b):
    return a + b


# маркируем как смоук-тест
@pytest.mark.smoke
def test_add():
    assert add_sum(2, 3) == 5, 'сумма не равна ожидаемой'


# маркируем как регрессионный тест
@pytest.mark.regression
def test_type_result():
    assert isinstance(add_sum(2, 3), int), \
        'не соответствует ожидаемому типу данных'


@pytest.mark.skip(reason="Тест устарел и требует переработки")
def test_old_functionality():
    assert False  # Этот тест не будет выполняться


@pytest.mark.xfail(reason="Баг в API, исправят в версии 2.5")
def test_broken_feature():
    assert add_sum(2, 3) == 6, 'сумма не равна ожидаемой'  # Сейчас падает


# ДЕКОРАТОР: регистрируем параметры в системе pytest
@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0)
])

# ФУНКЦИЯ: получаем конкретные значения для работы
def test_addition(x, y, expected):
    """
    Первый запуск: x=2, y=3, expected=5
    Второй запуск: x=0, y=0, expected=0  
    Третий запуск: x=-1, y=1, expected=0
    """
    result = x + y
    assert result == expected


# Использование фикстуры в тесте
def test_addition_with_fixture(sample_numbers):
    a, b, expected = sample_numbers
    assert a + b == expected, f"{a} + {b} должно быть {expected}"
