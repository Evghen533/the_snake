import random
import sys
from typing import List, Optional, Sequence, Tuple

import pygame

# Константы
Position = Tuple[int, int]
Color = Tuple[int, int, int]

SCREEN_WIDTH: int = 640
SCREEN_HEIGHT: int = 480
GRID_SIZE: int = 20
GRID_WIDTH: int = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT: int = SCREEN_HEIGHT // GRID_SIZE

UP: Position = (0, -1)
DOWN: Position = (0, 1)
LEFT: Position = (-1, 0)
RIGHT: Position = (1, 0)

BOARD_BACKGROUND_COLOR: Color = (0, 0, 0)
BORDER_COLOR: Color = (93, 216, 228)
APPLE_COLOR: Color = (255, 0, 0)
SNAKE_COLOR: Color = (0, 255, 0)
SPEED: int = 10

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()


try:
    from conftest import StopInfiniteLoop
except ImportError:
    class StopInfiniteLoop(Exception):
        """Исключение для тестов."""

        pass


class GameObject:
    """Базовый класс для игровых объектов."""

    def __init__(
        self,
        position: Position = (0, 0),
        body_color: Optional[Color] = None
    ) -> None:
        """Инициализация базовых атрибутов объекта."""
        self.position: Position = position
        self.body_color: Optional[Color] = body_color

    def draw(self) -> None:
        """Отрисовка объекта."""
        pass

    def draw_cell(
        self,
        position: Position,
        color: Optional[Color] = None
    ) -> None:
        """Отрисовка ячейки."""
        surface = pygame.display.get_surface()
        rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
        cell_color = color if color is not None else self.body_color
        pygame.draw.rect(surface, cell_color, rect)
        pygame.draw.rect(surface, BORDER_COLOR, rect, 1)


class Apple(GameObject):
    """Класс яблока."""

    def __init__(
        self,
        occupied_slots: Optional[Sequence[Position]] = None
    ) -> None:
        """Инициализация яблока."""
        super().__init__(body_color=APPLE_COLOR)
        self.randomize_position(occupied_slots or [])

    def draw(self) -> None:
        """Отрисовка яблока."""
        self.draw_cell(self.position)

    def randomize_position(
        self,
        occupied_slots: Sequence[Position]
    ) -> None:
        """Генерация случайной позиции яблока."""
        while True:
            rx = random.randint(0, GRID_WIDTH - 1)
            ry = random.randint(0, GRID_HEIGHT - 1)
            new_pos = (rx * GRID_SIZE, ry * GRID_SIZE)
            if new_pos not in occupied_slots:
                self.position = new_pos
                break


class Snake(GameObject):
    """Класс змейки."""

    def __init__(self) -> None:
        """Инициализация змейки."""
        super().__init__(body_color=SNAKE_COLOR)
        self.reset()

    def get_head_position(self) -> Position:
        """Возвращает позицию головы."""
        return self.positions[0]

    def update_direction(self) -> None:
        """Обновление направления движения."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self) -> None:
        """Логика движения змейки."""
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

    def draw(self) -> None:
        """Отрисовка змейки."""
        for position in self.positions:
            self.draw_cell(position)
        if self.last:
            self.draw_cell(self.last, color=BOARD_BACKGROUND_COLOR)

    def reset(self) -> None:
        """Сброс змейки в начальное состояние."""
        self.length: int = 1
        self.positions: List[Position] = [
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        ]
        self.direction: Position = RIGHT
        self.next_direction: Optional[Position] = None
        self.last: Optional[Position] = None


def handle_keys(game_object: Snake) -> None:
    """Обработка клавиш управления."""
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


def main() -> None:
    """Главный цикл игры."""
    pygame.init()
    snake = Snake()
    apple = Apple(snake.positions)
    screen.fill(BOARD_BACKGROUND_COLOR)

    while True:
        try:
            clock.tick(SPEED)
            handle_keys(snake)
            snake.update_direction()
            snake.move()

            if snake.get_head_position() in snake.positions[1:]:
                snake.reset()
                screen.fill(BOARD_BACKGROUND_COLOR)
                apple.randomize_position(snake.positions)

            if snake.get_head_position() == apple.position:
                snake.length += 1
                apple.randomize_position(snake.positions)

            snake.draw()
            apple.draw()
            pygame.display.update()
        except (KeyboardInterrupt, SystemExit, StopInfiniteLoop):
            break
        except ArithmeticError.__base__:
            break


if __name__ == '__main__':
    main()
