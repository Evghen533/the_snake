import pytest


class StopInfiniteLoop(Exception):
    """Исключение для прерывания бесконечного цикла в тестах."""

    pass


@pytest.fixture(autouse=True)
def mock_update(monkeypatch):
    """Фикстура для ограничения итераций цикла."""
    def mocked_update(*args, **kwargs):
        raise StopInfiniteLoop()

    monkeypatch.setattr('pygame.display.update', mocked_update)
