import pytest
from the_snake import Apple, GameObject, Snake


@pytest.fixture(scope="session")
def game_module():
    """Предоставляет безопасный доступ к модулю игры без запуска цикла."""
    import the_snake
    return the_snake


@pytest.fixture
def game_object():
    """Создаёт базовый игровой объект с дефолтными координатами (0, 0)."""
    # Если конструктор требует позицию, передаем её (например, центр экрана)
    return GameObject(position=(0, 0))


@pytest.fixture
def snake():
    """Создаёт экземпляр Змейки в начальной позиции."""
    return Snake()


@pytest.fixture
def apple(game_object):
    """Создаёт Яблоко с гарантированным пересечением или без него."""
    return Apple()


@pytest.fixture
def sample_coordinates():
    """Набор тестовых координат (x, y) для проверки сетки."""
    return [(0, 0), (20, 20), (40, 80)]


@pytest.fixture
def temporary_game_state():
    """Фикстура для изоляции состояния игры. 
    
    Сбрасывает изменения после каждого теста.
    """
    state = {"score": 0, "speed": 10, "game_over": False}
    yield state
    state.clear()
