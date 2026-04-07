import pytest
from the_snake import main


def test_main_run_without_exceptions():
    """Проверка запуска главного цикла."""
    try:
        main()
    except Exception as e:
        if 'StopInfiniteLoop' in str(type(e)):
            return
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
    except BaseException:
        pass
