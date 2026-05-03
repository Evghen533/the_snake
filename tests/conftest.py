import pytest


@pytest.fixture
def _the_snake():
    'Фикстура для доступа к модулю the_snake.'
    import the_snake
    return the_snake


@pytest.fixture
def game_object():
    'Фикстура для базового игрового объекта.'
    from the_snake import GameObject
    return GameObject()


@pytest.fixture
def snake():
    'Фикстура для объекта змейки.'
    from the_snake import Snake
    return Snake()


@pytest.fixture
def apple():
    'Фикстура для объекта яблока.'
    from the_snake import Apple
    return Apple()


@pytest.fixture
def sample_numbers():
    'Возвращает кортеж с числами для тестирования.'
    return (5, 10, 15)


@pytest.fixture(scope="session")
def temporary_data():
    '
    Фикстура с полным циклом: подготовка -> передача -> очистка
    '
    # ПОДГОТОВКА - выполняется ДО теста
    data = [1, 2, 3, 4, 5]
    print("Данные подготовлены:", data)

    # ПЕРЕДАЧА данных тесту
    yield data

    # ОЧИСТКА - выполняется ПОСЛЕ теста
    data.clear()  # данный метод очищает наш список
    print(f"{data} - пусто, данные очищены!")
