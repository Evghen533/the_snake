import pygame
import pytest

# Импортируем модули из корня. Если ваш файл называется main.py,
# замените `the_snake` на `main`.
from the_snake import (
    Apple,
    Snake,
    board_background_color,
    down,
    grid_size,
    left,
    right,
    screen_height,
    screen_width,
    up,
)


@pytest.fixture(autouse=True)
def init_pygame():
    """Автоматическая фикстура для инициализации виртуального экрана.

    Позволяет запускать тесты на сервере без графического интерфейса.
    """
    pygame.init()
    pygame.display.set_mode((1, 1), pygame.NOFRAME)
    yield
    pygame.quit()


@pytest.fixture
def snake():
    """Фикстура для создания чистого экземпляра змейки."""
    return Snake()


@pytest.fixture
def apple(snake):
    """Фикстура для создания яблока, учитывающая позицию змейки."""
    return Apple(occupied_slots=snake.positions)


def test_snake_initial_state(snake):
    """Проверяет корректность инициализации змейки."""
    assert snake.length == 1
    assert len(snake.positions) == 1
    assert snake.direction == right
    assert snake.get_head_position() == (
        screen_width // 2,
        screen_height // 2,
    )


def test_snake_movement(snake):
    """Проверяет шаг движения змейки вперед."""
    initial_head = snake.get_head_position()
    snake.move()
    new_head = snake.get_head_position()

    assert new_head == ((initial_head + grid_size) % screen_width, initial_head)


def test_snake_screen_wrapping(snake):
    """Проверяет прохождение змейки сквозь границы экрана."""
    snake.direction = right
    steps_to_edge = (screen_width // 2) // grid_size
    for _ in range(steps_to_edge + 1):
        snake.move()

    assert snake.get_head_position() == 0


def test_snake_direction_update(snake):
    """Проверяет смену направления движения."""
    snake.next_direction = up
    snake.update_direction()
    assert snake.direction == up


@pytest.mark.parametrize(
    "current_dir, forbidden_dir",
    [(right, left), (left, right), (up, down), (down, up)],
)
def test_snake_forbidden_turns(snake, current_dir, forbidden_dir):
    """Проверяет запрет разворота на 180 градусов."""
    snake.direction = current_dir
    snake.next_direction = forbidden_dir
    snake.update_direction()
    assert snake.direction == current_dir


def test_apple_generation(apple, snake):
    """Проверяет, что яблоко не генерируется внутри змейки."""
    for _ in range(50):
        apple.randomize_position(snake.positions)
        assert apple.position not in snake.positions


def test_eating_apple(snake, apple):
    """Моделирует логику роста змейки при поедании яблока."""
    head_x, head_y = snake.get_head_position()
    apple.position = ((head_x + grid_size) % screen_width, head_y)

    snake.move()

    if snake.get_head_position() == apple.position:
        snake.length += 1

    assert snake.length == 2
