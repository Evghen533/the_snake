import pytest
import pygame

from the_snake import main


def test_main_run_without_exceptions():
    """Проверка main на корректный выход по исключению."""
    try:
        main()
    except Exception as e:
        # Если название ошибки StopInfiniteLoop — значит всё круто, цикл прерван
        if type(e).__name__ == 'StopInfiniteLoop':
            return
        # Если это выход из системы — тоже Ок
        if isinstance(e, SystemExit):
            return
        # А вот если что-то другое — тогда заваливаем тест
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
