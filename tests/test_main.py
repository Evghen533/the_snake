import pytest

from conftest import StopInfiniteLoop
from the_snake import main


def test_main_run_without_exceptions():
    """Проверка, что main корректно завершается по сигналу StopInfiniteLoop."""
    try:
        main()
    except StopInfiniteLoop:
        # Это ожидаемый выход из цикла через фикстуру
        pass
    except SystemExit:
        # Это корректный системный выход
        pass
    except Exception as e:
        pytest.fail(f'Функция main завершилась с ошибкой: {e}')
