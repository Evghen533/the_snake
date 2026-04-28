import pytest


class StopInfiniteLoop(Exception):
    """Исключение для прерывания бесконечного цикла в тестах."""

    pass


@pytest.fixture(autouse=True)
def mock_update(monkeypatch):
    """Фикстура для ограничения количества итераций цикла."""
    stats = {'iterations': 0}
    max_iterations = 100

    def mocked_update(*args, **kwargs):
        stats['iterations'] += 1
        if stats['iterations'] > max_iterations:
            raise StopInfiniteLoop()

    monkeypatch.setattr('pygame.display.update', mocked_update)
