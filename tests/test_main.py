import pytest
from the_snake import main


def test_main_run_without_exceptions():
    """Проверка, что main корректно завершается по сигналу StopInfiniteLoop."""
    try:
        main()
    except Exception as e:
        # ПРОВЕРКА ПО ИМЕНИ: это решит проблему несовпадения объектов
        if type(e).__name__ == 'StopInfiniteLoop':
            return
        # Если это выход из системы — это тоже норма
        if isinstance(e, SystemExit):
            return
        # Любая другая ошибка — провал
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
