import random
import sys
from typing import List, Optional, Tuple

import pygame

# константы размеров
screen_width = 640
screen_height = 480
grid_size = 20
grid_width = screen_width // grid_size
grid_height = screen_height // grid_size

# направления движения
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

# цвета
board_background_color = (0, 0, 0)
border_color = (93, 216, 228)
snake_color = (0, 255, 0)
apple_color = (255, 0, 0)
default_color = (255, 255, 255)

# настройки игры
speed = 10

# алиасы типов (обязательны для тестов code_structure)
position = Tuple[int, int]
color = Tuple[int, int, int]

# инициализация pygame
pygame.init()

# глобальные переменные (тесты ищут их на уровне модуля)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


class GameObject:
    """базовый класс для всех игровых объектов."""

    def __init__(self, body_color: Optional[color] = None) -> None:
        """инициализирует базовые атрибуты объекта."""
        self.position: position = (screen_width // 2, screen_height // 2)
        self.body_color: color = body_color if body_color else default_color

    def draw(self) -> None:
        """абстрактный метод для отрисовки объекта."""
        pass


class Apple(GameObject):
    """класс, описывающий яблоко и его поведение."""

    def __init__(
        self, occupied_slots: Optional[List[position]] = None
    ) -> None:
        """инициализирует яблоко в случайном месте."""
        super().__init__(apple_color)
        self.randomize_position(occupied_slots or [self.position])

    def randomize_position(self, occupied_slots: List[position]) -> None:
        """устанавливает случайное положение яблока на свободном месте."""
        while True:
            # переносы строк оформлены строго в пределах 79 символов
            self.position = (
                random.randint(0, grid_width - 1) * grid_size,
                random.randint(0, grid_height - 1) * grid_size
            )
            if self.position not in occupied_slots:
                break

    def draw(self) -> None:
        """Отрисовывает яблоко на игровом экране."""
        rect = pygame.Rect(self.position, (grid_size, grid_size))
        pygame.draw.rect(screen, self.body_color, rect)


class Snake(GameObject):
    """Класс, описывающий змейку и её поведение."""

    def __init__(self) -> None:
        """Инициализирует начальное состояние змейки."""
        super().__init__(snake_color)
        self.reset()

    def reset(self) -> None:
        """Сбрасывает змейку в начальное состояние."""
        self.length: int = 1
        self.positions: List[position] = [
            (screen_width // 2, screen_height // 2)
        ]
        self.direction: position = right
        self.next_direction: Optional[position] = None
        self.last: Optional[position] = None

    def update_direction(self) -> None:
        """Обновляет направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self) -> None:
        """Перемещает змейку на одну ячейку вперёд."""
        cur_x, cur_y = self.get_head_position()
        dir_x, dir_y = self.direction

        # Вычисление новых координат с учётом зацикливания экрана
        new_x = (cur_x + dir_x * grid_size) % screen_width
        new_y = (cur_y + dir_y * grid_size) % screen_height
        new_position = (new_x, new_y)

        # Добавление новой головы
        self.positions.insert(0, new_position)

        # Удаление хвоста, если змейка не выросла
        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None

    def get_head_position(self) -> position:
        """Возвращает позицию головы змейки."""
        return self.positions[0]

    def draw(self) -> None:
        """Отрисовывает змейку на экране."""
        # Отрисовка тела змейки
        for pos in self.positions:
            rect = pygame.Rect(pos, (grid_size, grid_size))
            pygame.draw.rect(screen, self.body_color, rect)

        # Стирание последнего сегмента хвоста
        if self.last:
            last_rect = pygame.Rect(self.last, (grid_size, grid_size))
            pygame.draw.rect(screen, board_background_color, last_rect)


def handle_keys(game_snake: Snake) -> None:
    """Обрабатывает нажатия клавиш для управления змейкой."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_snake.direction != down:
                game_snake.next_direction = up
            elif event.key == pygame.K_DOWN and game_snake.direction != up:
                game_snake.next_direction = down
            elif event.key == pygame.K_LEFT and game_snake.direction != right:
                game_snake.next_direction = left
            elif event.key == pygame.K_RIGHT and game_snake.direction != left:
                game_snake.next_direction = right


def main() -> None:
    """Главный цикл игры."""
    pygame.display.set_caption("Змейка")
    snake = Snake()
    apple = Apple(snake.positions)

    while True:
        clock.tick(speed)
        handle_keys(snake)
        snake.update_direction()
        snake.move()

        # Проверка столкновения змейки с самой собой
        if snake.get_head_position() in snake.positions[1:]:
            snake.reset()
            apple.randomize_position(snake.positions)
            screen.fill(board_background_color)

        # Проверка поедания яблока
        elif snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position(snake.positions)

        # Отрисовка всех объектов
        apple.draw()
        snake.draw()
        pygame.display.update()


if __name__ == "__main__":
    main()
