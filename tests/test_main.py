import pytest

from the_snake import main


def test_main_run_without_exceptions():
    """Тест проверяет, что main корректно завершается по требованию."""
    try:
        main()
    except Exception as e:
        # Проверяем имя исключения как строку.
        # Это сработает, даже если объекты классов в памяти не совпали.
        if type(e).__name__ == 'StopInfiniteLoop':
            return
        if isinstance(e, SystemExit):
            return
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
