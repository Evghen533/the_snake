import pytest

# Важно: импортируем класс прямо из файла conftest
from conftest import StopInfiniteLoop
from the_snake import main


def test_main_run_without_exceptions():
    """Тест проверяет, что main корректно завершается по требованию."""
    try:
        main()
    except StopInfiniteLoop:
        # Тест поймал исключение и считает это успешным завершением
        pass
    except SystemExit:
        # Системный выход тоже считается успехом
        pass
    except Exception as e:
        # Любая другая ошибка — провал теста
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
