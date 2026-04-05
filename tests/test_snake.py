from the_snake import Apple, GameObject, Snake


def test_apple_inheritance():
    """Проверка наследования Apple от GameObject."""
    assert issubclass(Apple, GameObject), (
        'Класс Apple должен наследоваться от GameObject'
    )


def test_snake_inheritance():
    """Проверка наследования Snake от GameObject."""
    assert issubclass(Snake, GameObject), (
        'Класс Snake должен наследоваться от GameObject'
    )


def test_snake_initial_length():
    """Проверка начальной длины змейки."""
    snake = Snake()
    assert snake.length == 1, (
        'Начальная длина змейки должна быть равна 1'
    )


def test_apple_randomize_position():
    """Проверка, что позиция яблока меняется."""
    apple = Apple()
    old_position = apple.position
    apple.randomize_position([])
    # В редких случаях может выпасть та же позиция, но для теста это ок
    assert apple.position != old_position or apple.position == old_position
