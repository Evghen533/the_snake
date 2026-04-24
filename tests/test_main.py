import pytest

# Импортируем из conftest, чтобы перехват сработал на 100%
from conftest import StopInfiniteLoop
from the_snake import main


def test_main_run_without_exceptions():
    """Тест проверяет, что main корректно завершается по требованию."""
    try:
        main()
    except StopInfiniteLoop:
        # Теперь объекты совпадут, и исключение будет поймано здесь
        pass
    except Exception as e:
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
