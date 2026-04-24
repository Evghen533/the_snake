import pytest

# Важно: импортируем именно из conftest
from conftest import StopInfiniteLoop
from the_snake import main


def test_main_run_without_exceptions():
    """Тест проверяет, что main корректно завершается по требованию."""
    try:
        main()
    except StopInfiniteLoop:
        # Если поймали это исключение — тест пройден успешно
        pass
    except SystemExit:
        pass
    except Exception as e:
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
