import pytest


class StopInfiniteLoop(Exception):
    """Исключение для остановки бесконечного цикла в тестах."""

    pass


@pytest.fixture(autouse=True)
def mock_update(monkeypatch):
    """Подменяет pygame.display.update, чтобы прервать цикл."""
    def mocked_update(*args, **kwargs):
        raise StopInfiniteLoop()

    monkeypatch.setattr('pygame.display.update', mocked_update)
