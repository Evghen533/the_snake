import random

import pygame

# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)

BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)
SPEED = 10

# Инициализация pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()


try:
    from conftest import StopInfiniteLoop
except ImportError:
    class StopInfiniteLoop(Exception):
        """Заглушка для локального запуска."""

        pass


class GameObject:
    """Базовый класс для игровых объектов."""

    def __init__(self, position=(0, 0), body_color=None):
        """Инициализация базовых атрибутов объекта."""
        self.position = position
        self.body_color = body_color

    def draw(self):
        """Метод для отрисовки (переопределяется в подклассах)."""
        pass

    def draw_cell(self, position, color=None):
        """Отрисовка одной ячейки на поле."""
        surface = pygame.display.get_surface()
        rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, color or self.body_color, rect)
        pygame.draw.rect(surface, BORDER_COLOR, rect, 1)


class Apple(GameObject):
    """Класс, описывающий яблоко."""

    def __init__(self, occupied_slots=None):
        """Инициализация яблока."""
        super().__init__(body_color=APPLE_COLOR)
        self.randomize_position(occupied_slots or [])

    def draw(self):
        """Отрисовка яблока."""
        self.draw_cell(self.position)

    def randomize_position(self, occupied_slots):
        """Установка яблока в случайную свободную точку."""
        while True:
            new_pos = (
                random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
            )
            if new_pos not in occupied_slots:
                self.position = new_pos
                break


class Snake(GameObject):
    """Класс, описывающий змейку."""

    def __init__(self):
        """Инициализация змейки."""
        super().__init__(body_color=SNAKE_COLOR)
        self.reset()

    def get_head_position(self):
        """Возвращает координаты головы."""
        return self.positions[0]

    def update_direction(self):
        """Обновление направления движения."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Перемещение змейки."""
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
        """Отрисовка змейки."""
        for position in self.positions:
            self.draw_cell(position)

        if self.last:
            self.draw_cell(self.last, color=BOARD_BACKGROUND_COLOR)

    def reset(self):
        """Сброс змейки в начальное состояние."""
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None


def handle_keys(game_object):
    """Обработка ввода пользователя."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
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
            pygame.display.update()
        except (KeyboardInterrupt, SystemExit, StopInfiniteLoop):
            # Теперь StopInfiniteLoop — это тот самый объект из conftest
            break


if __name__ == '__main__':
    main()
