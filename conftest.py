import pytest


class StopInfiniteLoop(Exception):
    """Исключение для остановки цикла."""

    pass


@pytest.fixture(autouse=True)
def mock_update(monkeypatch):
    """Подменяет update для выхода из цикла."""
    def mocked_update(*args, **kwargs):
        raise StopInfiniteLoop()

    monkeypatch.setattr('pygame.display.update', mocked_update)
