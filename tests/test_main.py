import pytest
from conftest import StopInfiniteLoop
from the_snake import main

def test_main_run_without_exceptions():
    """Проверка запуска главного цикла без ошибок."""
    try:
        main()
    except StopInfiniteLoop:
        # ПЕРЕХВАТЫВАЕМ ТУТ: это значит, всё хорошо, игра запустилась!
        pass
    except SystemExit:
        pass
    except Exception as e:
        # Если ошибка НЕ StopInfiniteLoop, тогда валим тест
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
