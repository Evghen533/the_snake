import pytest

class StopInfiniteLoop(Exception):
    """Исключение для прерывания бесконечного цикла в тестах."""
    pass

@pytest.fixture(autouse=True)
def MockUpdate(monkeypatch):
    """Фикстура, которая ограничивает количество итераций цикла."""
    iterations = [0]
    max_iterations = 100  # Тест прервется после 100 обновлений экрана

    def mocked_update(*args, **kwargs):
        iterations[0] += 1
        if iterations[0] > max_iterations:
            raise StopInfiniteLoop()
    
    # Подменяем обновление экрана pygame на выброс исключения
    monkeypatch.setattr("pygame.display.update", mocked_update)
