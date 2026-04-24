import pytest

from the_snake import main


def test_main_run_without_exceptions():
    """Тест проверяет, что main корректно завершается по требованию."""
    try:
        main()
    except Exception as e:
        # Проверяем имя класса как строку. 
        # Это сработает, даже если объекты в памяти не совпали.
        if type(e).__name__ == 'StopInfiniteLoop':
            return
        # Если это выход из системы (sys.exit())
        if isinstance(e, SystemExit):
            return
        # Если прилетела любая другая реальная ошибка — валим тест
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
