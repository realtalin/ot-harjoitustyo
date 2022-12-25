import unittest
from unittest.mock import Mock
import pygame

from services.game.game import Game
from services.game.game_loop import GameLoop


class StubEvent:
    def __init__(self, event_type):
        self.type = event_type


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.score_service_mock = Mock()
        self.game = Game(800, self.score_service_mock)
        self.clock = Mock()
        self.clock.get_time = Mock(return_value=5000)
        self.event_queue = Mock()
        self.mouse = Mock()
        self.renderer = Mock()

    def test_score_is_saved_on_game_failure(self):
        self.game.game_over = Mock(return_value=True)
        self.game.save_score = Mock()

        events = [StubEvent(pygame.QUIT)]

        game_loop = GameLoop(self.game, self.clock,
                             StubEventQueue(events), self.mouse, self.renderer)

        game_loop.start()

        self.game.save_score.assert_called()
