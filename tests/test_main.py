import pytest
# Импортируем наше исключение, чтобы тест его "узнал"
from conftest import StopInfiniteLoop
from the_snake import main


def test_main_run_without_exceptions():
    """Проверка запуска главного цикла без ошибок."""
    try:
        main()
    except StopInfiniteLoop:
        # Если поймали это исключение — значит, main() дошел до отрисовки
        # и успешно начал работать. Это победа.
        pass
    except SystemExit:
        # Если вдруг сработал выход из системы
        pass
    except Exception as e:
        # Любая другая ошибка всё еще завалит тест
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
