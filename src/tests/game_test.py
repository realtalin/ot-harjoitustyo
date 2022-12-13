import unittest
from unittest.mock import Mock
from game.game import Game

DISPLAY_SIZE = 800


class TestGame(unittest.TestCase):
    
    def test_score_increases_by_one_on_level_success(self):
        game = Game(DISPLAY_SIZE)
        game.time = 5000
        game.new_level(5)
        game.level.all_correct_clicked = Mock(return_value=True)

        score_before_success = game.score
        game.update_state(5000)
        score_after_success = game.score

        self.assertEqual(score_before_success, 0)
        self.assertEqual(score_after_success, 1)

