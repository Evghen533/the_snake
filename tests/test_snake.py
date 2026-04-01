import sys
from pathlib import Path

# Добавляем корневую директорию в пути поиска модулей
sys.path.append(str(Path(__file__).parent.parent))

from the_snake import Snake


def test_snake_initial_length():
    """Тест начальной длины змейки."""
    snake = Snake()
    assert snake.length == 1
