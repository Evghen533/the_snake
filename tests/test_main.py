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
    assert isinstance(add_sum(2, 3), int), 'не соответствует ожидаемому типу данных'

@pytest.mark.skip(reason='Тест устарел и требует переработки')
def test_old_functionality():
    """Устаревший тест."""
    assert False

@pytest.mark.xfail(reason='Баг в API, исправят в версии 2.5. Тикет: BUG-123')
def test_broken_feature():
    """Тест с известной ошибкой."""
    assert add_sum(2, 3) == 6, 'сумма не равна ожидаемой'

@pytest.mark.parametrize('a, b, expected', [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -50, 50),
    (1.5, 2.5, 4.0)
])
def test_add_sum(a, b, expected):
    """Параметризованный тест функции add_sum."""
    assert add_sum(a, b) == expected

@pytest.fixture
def sample_numbers():
    return (2, 3, 5)

def test_addition_with_fixture(sample_numbers):
    """Тест с использованием фикстуры sample_numbers."""
    a, b, expected = sample_numbers
    assert add_sum(a, b) == expected, f'{a} + {b} должно быть {expected}'

def test_data_processing(temporary_data):
    """Проверка обработки временных данных без изменения оригинала."""
    original_data = temporary_data.copy()
    assert sum(original_data) == 15
    assert len(original_data) == 5

    modified_data = original_data + [6]
    assert sum(modified_data) == 21

def test_temporary_data_integrity(temporary_data):
    """Проверка целостности данных фикстуры."""
    assert temporary_data == [1, 2, 3, 4, 5]
