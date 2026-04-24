import pytest

from the_snake import main


def test_main_run_without_exceptions():
    """Тест проверяет, что main корректно завершается при прерывании."""
    try:
        main()
    except Exception as e:
        # Если название ошибки StopInfiniteLoop или SystemExit — это успех
        if type(e).__name__ == 'StopInfiniteLoop' or isinstance(e, SystemExit):
            return
        # А вот любая другая реальная ошибка — это провал
        pytest.fail(f'При запуске функции main возникло исключение: {e}')
