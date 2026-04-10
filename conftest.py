import pytest


class StopInfiniteLoop(Exception):
    """Исключение для остановки бесконечного цикла в тестах."""

    pass


@pytest.fixture(autouse=True)
def mock_infinite_loop(monkeypatch):
    """Фикстура для эмуляции остановки цикла."""
    pass
