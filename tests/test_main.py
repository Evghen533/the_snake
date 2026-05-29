from unittest.mock import patch
import pytest
from the_snake import main

def test_main_run_without_exceptions():
    """Тестирует запуск функции main."""
    with patch('pygame.display.update', side_effect=SystemExit), \
            pytest.raises(SystemExit):
        main()
