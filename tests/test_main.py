import pytest

from conftest import StopInfiniteLoop
from the_snake import main


def test_main_run_without_exceptions():
    """Проверка запуска главного цикла без ошибок."""
    try:
        main()
    except StopInfiniteLoop:
        # Если поймали это исключение — значит, main() дошел до отрисовки
        # и успешно начал работать. Это и есть прохождение теста.
        pass
    except SystemExit:
        # На случай, если сработал выход через pygame.quit()
        pass
    except Exception as e:
        # Любая другая ошибка всё еще должна завалить тест
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
