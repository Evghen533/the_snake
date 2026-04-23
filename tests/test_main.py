import pytest

from conftest import StopInfiniteLoop
from the_snake import main


def test_main_run_without_exceptions():
    """Тест проверяет корректное прерывание функции main."""
    try:
        main()
    except StopInfiniteLoop:
        # Ожидаемое поведение: фикстура прервала цикл
        pass
    except SystemExit:
        # Также допустимый вариант выхода
        pass
    except Exception as e:
        pytest.fail(f'Функция main завершилась с ошибкой: {e}')
