import pytest


@pytest.fixture
def _the_snake():
    """Фикстура для доступа к модулю the_snake."""

    import the_snake
    return the_snake


@pytest.fixture(scope='session')
def temporary_data():
    """Фикстура с полным циклом: подготовка -> передача -> очистка."""

    data = [1, 2, 3, 4, 5]
    yield data
    data.clear()
