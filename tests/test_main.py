import pytest
import pygame
from conftest import StopInfiniteLoop
from the_snake import main

def test_main_run_without_exceptions():
    """Проверка, что main() корректно обрабатывает завершение цикла."""
    try:
        main()
    except StopInfiniteLoop:
        # Это ожидаемое поведение: тест прервал цикл
        pass
    except SystemExit:
        # Это тоже корректный выход
        pass
    except Exception as e:
        pytest.fail(f"Функция main завершилась с необработанной ошибкой: {type(e).__name__}: {e}")
