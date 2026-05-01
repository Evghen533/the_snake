import pytest


@pytest.fixture
def sample_numbers():
    """Возвращает кортеж с числами для тестирования."""
    return (5, 10, 15)
