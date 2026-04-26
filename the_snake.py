import random
import sys
from typing import List, Optional, Tuple

import pygame

# Константы
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвета
BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228)
SNAKE_COLOR = (0, 255, 0)
APPLE_COLOR = (255, 0, 0)
DEFAULT_COLOR = (255, 255, 255)

# Скорость игры
SPEED = 10

# Типы для аннотаций
Position = Tuple[int, int]

# Инициализация pygame
pygame.init()

# Глобальные переменные
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


class StopInfiniteLoop(Exception):
    """Исключение для остановки цикла."""

    pass


class GameObject:
    """Базовый класс для всех игровых объектов."""

    def __init__(self, color: Optional[Tuple[int, int, int]] = None):
        """Инициализирует базовые атрибуты объекта."""
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = color if color else DEFAULT_COLOR

    def draw(self):
        """Абстрактный метод для отрисовки объекта."""
        pass

    def draw_cell(self, position: Position, color: Optional[tuple] = None):
        """Отрисовывает одну ячейку на игровом поле."""
        rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, color or self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Apple(GameObject):
    """Класс, описывающий яблоко и его поведение."""

    def __init__(self, occupied_slots: Optional[List[Position]] = None):
        """Инициализирует яблоко в случайном месте."""
        super().__init__(APPLE_COLOR)
        self.randomize_position(occupied_slots or [self.position])

    def randomize_position(self, occupied_slots: List[Position]):
        """Устанавливает случайное положение яблока на свободном месте."""
        while True:
            self.position = (
                random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
            )
            if self.position not in occupied_slots:
                break

    def draw(self):
        """Отрисовывает яблоко на экране."""
        self.draw_cell(self.position)


class Snake(GameObject):
    """Класс, описывающий змейку и её механику."""

    def __init__(self):
        """Инициализирует начальное состояние змейки."""
        super().__init__(SNAKE_COLOR)
        self.reset()

    def reset(self):
        """Сбрасывает змейку в начальное состояние."""
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None

    def get_head_position(self) -> Position:
        """Возвращает позицию головы змейки."""
        return self.positions[0]

    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Обновляет позицию змейки, добавляя новую голову."""
        head_x, head_y = self.get_head_position()
        dx, dy = self.direction
        new_pos = (
            (head_x + dx * GRID_SIZE) % SCREEN_WIDTH,
            (head_y + dy * GRID_SIZE) % SCREEN_HEIGHT
        )

        self.positions.insert(0, new_pos)
        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None

    def draw(self):
        """Отрисовывает змейку, затирая последний сегмент."""
        for position in self.positions:
            self.draw_cell(position)

        if self.last:
            self.draw_cell(self.last, color=BOARD_BACKGROUND_COLOR)


def handle_keys(game_object: Snake):
    """Обрабатывает нажатия клавиш для управления змейкой."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Главный цикл игры."""
    snake = Snake()
    apple = Apple(snake.positions)

    while True:
        try:
            clock.tick(SPEED)
            handle_keys(snake)
            snake.update_direction()
            snake.move()
            if snake.get_head_position() == apple.position:
                snake.length += 1
                apple.randomize_position(snake.positions)
            if snake.get_head_position() in snake.positions[1:]:
                snake.reset()
            screen.fill(BOARD_BACKGROUND_COLOR)
            apple.draw()
            snake.draw()
            pygame.display.update()  # <-- Здесь pytest бросит исключение
        except (KeyboardInterrupt, SystemExit):
            # Ловим только системные сигналы выхода
            break
        # Больше никаких except здесь быть не должно!


if __name__ == '__main__':
    main()
