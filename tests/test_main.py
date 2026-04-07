import pytest
# Импортируем наше исключение из conftest
from conftest import StopInfiniteLoop
from the_snake import main


def test_main_run_without_exceptions():
    """Проверка запуска главного цикла."""
    try:
        main()
    except StopInfiniteLoop:
        # Это значит, что фикстура успешно остановила бесконечный цикл
        pass
    except SystemExit:
        # Это если сработал sys.exit()
        pass
    except Exception as e:
        # А вот любая другая ошибка — это уже повод завалить тест
        pytest.fail(f"При запуске функции main возникло исключение: {e}")
