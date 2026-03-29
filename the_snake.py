import random
import sys
from typing import List, Optional, Tuple

import pygame

# Константы
SCREEN_WIDTH: int = 640
SCREEN_HEIGHT: int = 480
GRID_SIZE: int = 20
GRID_WIDTH: int = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT: int = SCREEN_HEIGHT // GRID_SIZE

UP: Tuple[int, int] = (0, -1)
DOWN: Tuple[int, int] = (0, 1)
LEFT: Tuple[int, int] = (-1, 0)
RIGHT: Tuple[int, int] = (1, 0)

BOARD_BACKGROUND_COLOR: Tuple[int, int, int] = (0, 0, 0)
BORDER_COLOR: Tuple[int, int, int] = (93, 216, 228)
APPLE_COLOR: Tuple[int, int, int] = (255, 0, 0)
SNAKE_COLOR: Tuple[int, int, int] = (0, 255, 0)
SPEED: int = 10

screen: pygame.Surface = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32
)
pygame.display.set_caption('Змейка')
clock: pygame.time.Clock = pygame.time.Clock()


class GameObject:
    """Базовый класс для игровых объектов."""

    def __init__(
        self,
        position: Tuple[int, int] = (0, 0),
        body_color: Optional[Tuple[int, int, int]] = None
    ) -> None:
        """Инициализация базовых атрибутов объекта."""
        self.position: Tuple[int, int] = position
        self.body_color: Optional[Tuple[int, int, int]] = body_color

    def draw(self) -> None:
        """Абстрактный метод для отрисовки."""
        raise NotImplementedError(
            'Метод draw() должен быть переопределен в дочернем классе'
        )

    def draw_cell(
        self,
        position: Tuple[int, int],
        color: Optional[Tuple[int, int, int]] = None
    ) -> None:
        """Общий метод для отрисовки одной ячейки."""
        rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, color or self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Apple(GameObject):
    """Класс яблока."""

    def __init__(
        self,
        occupied_slots: Optional[List[Tuple[int, int]]] = None
    ) -> None:
        """Инициализация яблока."""
        super().__init__(body_color=APPLE_COLOR)
        self.randomize_position(occupied_slots or [])

    def draw(self) -> None:
        """Отрисовка яблока."""
        self.draw_cell(self.position)

    def randomize_position(
        self, occupied_slots: List[Tuple[int, int]]
    ) -> None:
        """Генерация случайной позиции, не занятой змейкой."""
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
        """Инициализация змейки через reset."""
        super().__init__(body_color=SNAKE_COLOR)
        self.reset()

    def get_head_position(self) -> Tuple[int, int]:
        """Координаты головы (первый элемент списка)."""
        return self.positions[0]

    def update_direction(self) -> None:
        """Обновление направления."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self) -> None:
        """Логика движения. Только перемещение без проверок."""
        head_x, head_y = self.get_head_position()
        dx, dy = self.direction
        new_pos: Tuple[int, int] = (
            (head_x + dx * GRID_SIZE) % SCREEN_WIDTH,
            (head_y + dy * GRID_SIZE) % SCREEN_HEIGHT
        )
        # Просто добавляем новую голову
        self.positions.insert(0, new_pos)
        # И удаляем хвост
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
        self.positions: List[Tuple[int, int]] = [
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        ]
        self.direction: Tuple[int, int] = RIGHT
        self.next_direction: Optional[Tuple[int, int]] = None
        self.last: Optional[Tuple[int, int]] = None


def handle_keys(game_object: Snake) -> None:
    """Обработка клавиш."""
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
    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.update_direction()

        # Рассчитываем следующую позицию для проверки
        head_x, head_y = snake.get_head_position()
        dx, dy = snake.direction
        next_pos = (
            (head_x + dx * GRID_SIZE) % SCREEN_WIDTH,
            (head_y + dy * GRID_SIZE) % SCREEN_HEIGHT
        )

        # ПРОВЕРКА СТОЛКНОВЕНИЯ ПЕРЕД ДВИЖЕНИЕМ
        if next_pos in snake.positions:
            snake.reset()
            screen.fill(BOARD_BACKGROUND_COLOR)
            apple.randomize_position(snake.positions)
        else:
            snake.move()

        # Проверка поедания яблока
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position(snake.positions)

        snake.draw()
        apple.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
    
