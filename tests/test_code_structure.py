import pygame
from the_snake import Apple, GameObject, Snake


def test_game_object_attributes():
    """Проверка атрибутов GameObject."""
    obj = GameObject()
    assert hasattr(obj, 'position'), 'У GameObject должен быть атрибут position'
    assert hasattr(obj, 'body_color'), 'У GameObject должен быть атрибут body_color'
    assert hasattr(obj, 'draw'), 'У GameObject должен быть метод draw'


def test_apple_inheritance():
    """Проверка, что Apple наследуется от GameObject."""
    assert issubclass(Apple, GameObject), 'Apple должен наследоваться от GameObject'


def test_snake_inheritance():
    """Проверка, что Snake наследуется от GameObject."""
    assert issubclass(Snake, GameObject), 'Snake должен наследоваться от GameObject'


def test_snake_initial_length():
    """Проверка начальной длины змейки."""
    snake = Snake()
    assert snake.length == 1, 'Начальная длина змейки должна быть 1'
