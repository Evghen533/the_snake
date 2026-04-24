import pytest


@pytest.fixture
def sample_numbers():
    """Возвращает кортеж с числами для тестирования"""
    return (5, 10, 15)


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


@pytest.fixture
def temporary_data():
    """
    Фикстура с полным циклом: подготовка -> передача -> очистка
    """
    # ПОДГОТОВКА - выполняется ДО теста
    data = [1, 2, 3, 4, 5]
    print("Данные подготовлены:", data)

    # ПЕРЕДАЧА данных тесту
    yield data

    # ОЧИСТКА - выполняется ПОСЛЕ теста
    data.clear()  # данный метод очищает наш список
    print(f"{data} - пусто, данные очищены!")
