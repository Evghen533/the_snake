import pytest
from conftest import StopInfiniteLoop
from the_snake import main

def test_main_run_without_exceptions():
    try:
        main()
    except StopInfiniteLoop:
        pass
    except SystemExit:
        pass
    except Exception as e:
        pytest.fail(f'Ошибка в main: {e}')
