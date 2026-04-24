import pytest

from conftest import StopInfiniteLoop
from the_snake import main


def test_main_run_without_exceptions():
    """Проверка main на корректный выход по исключению."""
    try:
        main()
    except StopInfiniteLoop:
        # Тест пройдет, если поймает это специфичное исключение
        pass
    except Exception as e:
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
