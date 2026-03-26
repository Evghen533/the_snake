from the_snake import Snake

def test_snake_initial_length():
    snake = Snake()
    assert snake.length == 1
