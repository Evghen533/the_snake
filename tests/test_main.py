import pytest

from conftest import StopInfiniteLoop
from the_snake import main


def test_main_run_without_exceptions():
    """Проверка запуска главного цикла без ошибок."""
    try:
        main()
    except StopInfiniteLoop:
        # Это нормальное поведение: мы сами прервали цикл через conftest
        pass
    except SystemExit:
        # Это если сработал sys.exit() при закрытии окна
        pass
    except Exception as e:
        # Любая другая реальная ошибка завалит тест
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
