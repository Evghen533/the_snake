import pytest

# Импортируем тот самый класс, чтобы перехват сработал
from conftest import StopInfiniteLoop
from the_snake import main


def test_main_run_without_exceptions():
    """Тест проверяет корректное прерывание функции main."""
    try:
        main()
    except StopInfiniteLoop:
        # Теперь объекты совпадут, и тест увидит, что исключение поймано
        pass
    except SystemExit:
        pass
    except Exception as e:
        # Если исключение не узнано, оно упадет сюда и вызовет fail
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
