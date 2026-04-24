import pytest

# Пытаемся импортировать так, чтобы объект совпал с conftest
try:
    from conftest import StopInfiniteLoop
except ImportError:
    from .conftest import StopInfiniteLoop

from the_snake import main


def test_main_run_without_exceptions():
    """Тест проверяет, что main корректно завершается по требованию."""
    try:
        main()
    except StopInfiniteLoop:
        pass
    except SystemExit:
        pass
    except Exception as e:
        # Любая другая ошибка (или если StopInfiniteLoop не узнан) — провал
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
