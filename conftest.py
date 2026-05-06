import pytest

import the_snake
from the_snake import Apple, GameObject, Snake


@pytest.fixture
def _the_snake():
    """Предоставляет доступ к модулю the_snake."""
    return the_snake


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
    """Набор тестовых чисел."""
    return (5, 10, 15)


@pytest.fixture
def temporary_data():
    """Временные данные с очисткой после теста."""
    data = [1, 2, 3, 4, 5]
    yield data
    data.clear()
