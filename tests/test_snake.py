from the_snake import Snake


def test_snake_initial_length():
    """Тест начальной длины змейки."""
    snake = Snake()
    assert snake.length == 1
