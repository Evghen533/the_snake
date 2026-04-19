import pytest


class StopInfiniteLoop(Exception):
    """Исключение для прерывания бесконечного цикла в тестах."""

    pass


@pytest.fixture(autouse=True)
def mock_update(monkeypatch):
    """Фикстура, которая ограничивает количество итераций цикла."""
    iterations = [0]
    max_iterations = 100

    def mocked_update(*args, **kwargs):
        iterations[0] += 1
        if iterations[0] > max_iterations:
            raise StopInfiniteLoop()

    monkeypatch.setattr('pygame.display.update', mocked_update)
