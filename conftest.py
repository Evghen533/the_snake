fimport pytest


@pytest.fixture
def sample_numbers():
    """Возвращает кортеж с числами для тестирования"""
    return (5, 10, 15)

@pytest.fixture
def _the_snake():
    """Предоставляет доступ к самому модулю игры для структурных тестов."""
    return the_snake


@pytest.fixture
def game_object():
    """Создаёт базовый экземпляр GameObject для тестов структуры."""
    return GameObject()


@pytest.fixture
def snake():
    """Создаёт чистый экземпляр Snake для каждого теста."""
    return Snake()


@pytest.fixture
def apple():
    """Создаёт экземпляр Apple с дефолтными свободными слотами."""
    return Apple()


@pytest.fixture
def sample_numbers():
    """Набор тестовых чисел для математических тестов."""
    return (5, 10, 15)


@pytest.fixture
def temporary_data():
    """Возвращает список данных, изолированный для каждого теста."""
    return [1, 2, 3, 4, 5]
