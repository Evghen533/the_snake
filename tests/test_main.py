import pytest
from the_snake import main


def test_main_run_without_exceptions():
    """Тест проверяет, что main корректно завершается по требованию."""
    try:
        main()
    except Exception as e:
        # Проверяем имя класса строкой. 
        # Это поймает StopInfiniteLoop, даже если объекты не совпали.
        if type(e).__name__ == 'StopInfiniteLoop':
            return
        # Если это стандартный выход из Pygame
        if isinstance(e, SystemExit):
            return
        # Если прилетела какая-то другая ошибка — валим тест
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
