import os

import pytest

# Устанавливаем драйвер до импорта pygame
os.environ['SDL_VIDEODRIVER'] = 'dummy'

import pygame  # noqa: E402


class StopInfiniteLoop(Exception):
    """Исключение для остановки бесконечного цикла в тестах."""

    pass


@pytest.fixture(autouse=True)
def mock_infinite_loop(monkeypatch):
    """Фикстура для эмуляции остановки цикла."""
    def mock_update(*args, **kwargs):
        raise StopInfiniteLoop

    monkeypatch.setattr(pygame.display, 'update', mock_update)

    # Используем одинарные кавычки, как просит линтер (Q000)
    monkeypatch.setattr(pygame.display, 'update', mock_update)


@pytest.fixture(autouse=True)
def mock_random(monkeypatch):
    """Фикстура для фиксации рандома, если это нужно тестам."""
    random.seed(42)
