import pytest
import os

# Принудительно отключаем окно для всех тестов
os.environ['SDL_VIDEODRIVER'] = 'dummy'

@pytest.fixture
def _the_snake():
    """Фикстура для импорта модуля игры."""
    import the_snake
    return the_snake

@pytest.fixture
def game_object(_the_snake):
    """Фикстура для базового объекта."""
    return _the_snake.GameObject()

@pytest.fixture
def apple(_the_snake):
    """Фикстура для яблока (нужна тестам!)."""
    return _the_snake.Apple()

@pytest.fixture
def snake(_the_snake):
    """Фикстура для змейки (нужна тестам!)."""
    return _the_snake.Snake()

class StopInfiniteLoop(Exception):
    pass

@pytest.fixture(autouse=True)
def stop_main_loop(monkeypatch):
    """Фикстура для остановки бесконечного цикла."""
    import pygame
    def mock_update():
        raise StopInfiniteLoop
    monkeypatch.setattr(pygame.display, "update", mock_update)
