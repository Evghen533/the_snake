from unittest.mock import MagicMock

import pytest

from the_snake import Apple, Snake


@pytest.fixture(autouse=True)
def mock_pygame(monkeypatch):
    """Изолирует тесты от реального графического интерфейса pygame."""
    mock_display = MagicMock()
    monkeypatch.setattr('pygame.display.set_mode', mock_display)
    monkeypatch.setattr('pygame.display.set_caption', MagicMock())
    monkeypatch.setattr('pygame.display.update', MagicMock())
    monkeypatch.setattr('pygame.draw.rect', MagicMock())
    monkeypatch.setattr('pygame.init', MagicMock())
    return mock_display


@pytest.fixture
def snake():
    """Создаёт чистый экземпляр Snake для каждого теста."""
    return Snake()


@pytest.fixture
def apple(snake):
    """Создаёт экземпляр Apple, учитывая занятые змейкой координаты."""
    return Apple(occupied_slots=snake.positions)


@pytest.fixture
def sample_numbers():
    """Набор тестовых чисел."""
    return (5, 10, 15)


@pytest.fixture(scope='session')
def temporary_data():
    """Возвращает список данных, общий для всей тестовой сессии."""
    return [1, 2, 3, 4, 5]
