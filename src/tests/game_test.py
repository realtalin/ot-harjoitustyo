import unittest
from unittest.mock import Mock

from services.game.game import Game

VISUAL_GRID_SIZE = 800


class TestGame(unittest.TestCase):
    def setUp(self):
        self.score_service_mock = Mock()
        self.time = 5000
        self.game = Game(VISUAL_GRID_SIZE, self.score_service_mock)
        self.game.reset(self.time)
        

    def test_score_increases_by_one_on_level_success(self):
        self.game.level.all_correct_clicked = Mock(return_value=True)

        score_before_success = self.game.score
        self.game.update_state(self.time)
        score_after_success = self.game.score

        self.assertEqual(score_before_success, 0)
        self.assertEqual(score_after_success, 1)

    def test_game_is_over_after_exactly_three_incorrect_clicks(self):
        mouse_pos = (100, 100)
        
        self.assertEqual(self.game.game_over(), False)

        self.game.level.click_on_incorrect_cell = Mock(return_value=True)
        self.game.click(mouse_pos, self.time)

        self.assertEqual(self.game.game_over(), False)

        self.game.level.click_on_incorrect_cell = Mock(return_value=True)
        self.game.click(mouse_pos, self.time)

        self.assertEqual(self.game.game_over(), False)

        self.game.level.click_on_incorrect_cell = Mock(return_value=True)
        self.game.click(mouse_pos, self.time)

        self.assertEqual(self.game.game_over(), True)
