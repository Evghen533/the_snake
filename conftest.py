import os
import pytest

# 1. Устанавливаем переменную ДО импортов pygame
os.environ['SDL_VIDEODRIVER'] = 'dummy'

import pygame

class StopInfiniteLoop(Exception):
    """Исключение для остановки бесконечного цикла в тестах."""
    pass

@pytest.fixture(autouse=True)
def mock_infinite_loop(monkeypatch):
    """Фикстура для эмуляции остановки цикла."""
    def mock_update(*args, **kwargs):
        raise StopInfiniteLoop
    
    # Подменяем обновление экрана, чтобы цикл прервался на первой итерации
    monkeypatch.setattr(pygame.display, "update", mock_update)
