import pytest
from conftest import StopInfiniteLoop
from the_snake import main


def test_main_run_without_exceptions():
    """Проверка запуска главного цикла без ошибок."""
    try:
        main()
    except StopInfiniteLoop:
        # Это нормальное поведение: тест сам остановил цикл
        pass
    except SystemExit:
        # Если pygame.quit() сработал
        pass
    except Exception as e:
        pytest.fail(f"При запуске функции main возникло исключение: {e}")
