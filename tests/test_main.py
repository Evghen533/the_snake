import pytest


def add_sum(a, b):
    """Возвращает сумму двух чисел."""
    return a + b


@pytest.mark.smoke
def test_add():
    """Тест сложения (smoke)."""
    assert add_sum(2, 3) == 5, 'сумма не равна ожидаемой'


@pytest.mark.regression
def test_type_result():
    """Тест типа данных (regression)."""
    assert isinstance(add_sum(2, 3), int), \
        'не соответствует ожидаемому типу данных'


@pytest.mark.skip(reason='Тест устарел и требует переработки')
def test_old_functionality():
    """Устаревший тест."""
    assert False


@pytest.mark.xfail(reason='Баг в API, исправят в версии 2.5')
def test_broken_feature():
    """Тест с известной ошибкой."""
    assert add_sum(2, 3) == 6, 'сумма не равна ожидаемой'


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0)
    ]
)
def test_addition(x, y, expected):
    """Параметризованный тест сложения."""
    result = add_sum(x, y)
    assert result == expected
