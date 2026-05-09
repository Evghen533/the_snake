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


def test_data_processing(temporary_data):
    """
    Тест использует данные из фикстуры и проверяет их обработку
    """
    print("Начало теста № 1 - данные:", temporary_data)

    # Проверяем сумму
    assert sum(temporary_data) == 15

    # Проверяем количество элементов
    assert len(temporary_data) == 5

    # Модифицируем данные (это безопасно - после теста они очистятся)
    temporary_data.append(6)
    print("Данные изменены:", temporary_data)

    print("Тест № 1 завершён")


def test_data_after_session_fixture(temporary_data):
    """
    Тест использует данные из фикстуры и проверяет их обработку
    """
    print("Начало теста № 2 - данные:", temporary_data)

    # Проверяем сумму
    assert temporary_data == [1, 2, 3, 4, 5]
    print("Тест № 2 завершён")
