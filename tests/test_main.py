import pytest

from conftest import StopInfiniteLoop
from the_snake import main


def test_main_run_without_exceptions():
    """Тест проверяет, что main корректно завершается при прерывании."""
    try:
        main()
    except StopInfiniteLoop:
        pass
    except SystemExit:
        pass
    except Exception as e:
        pytest.fail(f'Функция main завершилась с ошибкой: {e}')
