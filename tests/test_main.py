import pytest

# Импортируем исключение прямо из conftest, чтобы объекты совпали
from conftest import StopInfiniteLoop
from the_snake import main


def test_main_run_without_exceptions():
    """Тест проверяет, что main корректно завершается по требованию."""
    try:
        main()
    except StopInfiniteLoop:
        # Если поймали это исключение — это успех, цикл остановился
        pass
    except SystemExit:
        # Это тоже корректный выход
        pass
    except Exception as e:
        # А вот любая другая ошибка — это провал
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
