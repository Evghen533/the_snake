import pytest
from the_snake import main


@pytest.mark.timeout(1)
def test_main_run_without_exceptions():
    """Проверка запуска главного цикла."""
    try:
        main()
    except SystemExit:
        pass
    except Exception as e:
        pytest.fail(f"Функция main() вызвала исключение: {e}")
