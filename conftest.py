import pytest


@pytest.fixture
def _the_snake():
    import the_snake
    return the_snake


@pytest.fixture
def game_object():
    from the_snake import GameObject
    return GameObject()


@pytest.fixture
def snake():
    from the_snake import Snake
    return Snake()


@pytest.fixture
def apple():
    from the_snake import Apple
    return Apple()


@pytest.fixture
def sample_numbers():
    return (5, 10, 15)


@pytest.fixture
def temporary_data():
    data = [1, 2, 3, 4, 5]
    yield data
    data.clear()
