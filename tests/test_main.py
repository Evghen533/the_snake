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
    assert isinstance(
        add_sum(2, 3), int
    ), 'не соответствует ожидаемому типу данных'


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


def test_data_processing(temporary_data):
    """Тест проверяет обработку данных из фикстуры."""
    data_copy = temporary_data.copy()
    assert sum(data_copy) == 15
    assert len(data_copy) == 5
    data_copy.append(6)


def test_data_after_session_fixture(temporary_data):
    """Проверка данных после использования в другом тесте."""
    assert temporary_data == [1, 2, 3, 4, 5]
