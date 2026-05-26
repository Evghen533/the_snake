from unittest.mock import MagicMock

import pytest

import the_snake
from the_snake import Apple, GameObject, Snake


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
def _the_snake():
    """Предоставляет доступ к самому модулю игры для структурных тестов."""
    return the_snake


@pytest.fixture
def game_object():
    """Создаёт базовый экземпляр GameObject для тестов структуры."""
    return GameObject()


@pytest.fixture
def snake():
    """Создаёт чистый экземпляр Snake для каждого теста."""
    return Snake()


@pytest.fixture
def apple():
    """Создаёт экземпляр Apple с дефолтными свободными слотами."""
    return Apple()


@pytest.fixture
def sample_numbers():
    """Набор тестовых чисел для математических тестов."""
    return (5, 10, 15)


@pytest.fixture(scope='session')
def temporary_data():
    """Возвращает список данных, общий для всей тестовой сессии."""
    return
