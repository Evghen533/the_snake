import os
import pytest

os.environ['SDL_VIDEODRIVER'] = 'dummy'

import pygame

class StopInfiniteLoop(Exception):
    pass

@pytest.fixture(autouse=True)
def mock_infinite_loop(monkeypatch):
    def mock_update(*args, **kwargs):
        raise StopInfiniteLoop
    monkeypatch.setattr(pygame.display, "update", mock_update)
