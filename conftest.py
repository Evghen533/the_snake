import pytest

import the_snake
from the_snake import Apple, GameObject, Snake


@pytest.fixture(scope="module")
def snake():
    """Создаёт экземпляр Snake один раз на модуль."""
    return Snake()


@pytest.fixture
def game_object():
    """Создаёт экземпляр GameObject."""
    return GameObject()


@pytest.fixture
def snake():
    """Создаёт экземпляр Snake."""
    return Snake()


@pytest.fixture
def apple():
    """Создаёт экземпляр Apple."""
    return Apple()


@pytest.fixture
def sample_numbers():
    """Набор тестовых чисел, включая граничные случаи."""
    return (-10, 0, 5, 10, 15, 100)


@pytest.fixture
def temporary_data():
    """Временные данные с очисткой после теста.

    Пример использования:
    - Тестирование функций, модифицирующих списки.
    - Проверка граничных условий обработки данных.
    """
    data = [1, 2, 3, 4, 5]
    yield data
    data.clear()
