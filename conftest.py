import os
import sys
import pygame
import pytest

# Гарантируем, что корень репозитория находится в sys.path.
# Это избавит от ошибок "ModuleNotFoundError" при импортах в тестах.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture(scope="session", autouse=True)
def init_virtual_pygame():
    """Автоматически инициализирует виртуальный дисплей Pygame.
    
    Действует на протяжении всей сессии тестов. Позволяет запускать
    тесты на серверах проверки (CI/CD) без графической оболочки.
    """
    pygame.init()
    pygame.display.set_mode((1, 1), pygame.NOFRAME)
    yield
    pygame.quit()


def pytest_configure(config):
    """Регистрирует кастомные маркеры проекта.
    
    Убирает предупреждения (warnings) в консоли при использовании 
    маркеров @pytest.mark.smoke и @pytest.mark.regression.
    """
    config.addinivalue_line(
        "markers", "smoke: быстрые тесты критического функционала"
    )
    config.addinivalue_line(
        "markers", "regression: тесты регрессии"
    )
