import pytest

from the_snake import GameObject, Snake, Apple



@pytest.fixture
def the_snake_module():
    """Предоставляет доступ к модулю the_snake."""
    import the_snake
    return the_snake



@pytest.fixture
def game_object():
    """Создаёт GameObject с корректными параметрами."""
    return GameObject(position=(0, 0), body_color=(255, 255, 255))



@pytest.fixture
def snake():
    """Создаёт экземпляр змейки с начальными параметрами."""
    return Snake()



@pytest.fixture
def snake_with_length():
    """Фабрика для создания змейки заданной длины."""
    def _create_snake(length=1):
        snake = Snake()
        snake.length = length
        head_x, head_y = snake.get_head_position()
        snake.positions = [(head_x - i * 20, head_y) for i in range(length)]
        return snake
    return _create_snake



@pytest.fixture
def apple():
    """Фабрика для создания яблока с возможностью задать позицию."""
    def _create_apple(position=None):
        apple = Apple()
        if position:
            apple.position = position
        return apple
    return _create_apple



@pytest.fixture
def sample_numbers():
    """Набор тестовых чисел для параметризованных тестов."""
    return (5, 10, 15)



@pytest.fixture(scope='function')
def clean_snake():
    """Змейка, которая сбрасывается после каждого теста."""
    snake = Snake()
    yield snake
    # Дополнительная очистка, если нужна
    snake.reset()
