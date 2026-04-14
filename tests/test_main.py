import pytest
import pygame

def test_main_run_without_exceptions():
    # Инициализируем Pygame для теста
    if not pygame.get_init():
        pygame.init()

    try:
        main()  # функция должна завершиться без исключений
    except Exception as e:
        pytest.fail(f"Функция main завершилась с исключением: {e}")
    finally:
        # Гарантированно завершаем Pygame после теста
        if pygame.get_init():
            pygame.quit()
