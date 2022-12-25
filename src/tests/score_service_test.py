import unittest
from unittest.mock import Mock
from services.database.score_service import ScoreService


class TestScoreService(unittest.TestCase):
    def setUp(self):
        self.score_repository = Mock()
        self.score_service = ScoreService(self.score_repository)

    def test_save(self):
        self.score_service.fetch_all()
        self.score_repository.fetch_all.assert_called_once()

    def test_save_with_valid_score(self):
        self.score_service.save('jaakko', 3)

        self.score_repository.save.assert_called_once_with(
            {'username': 'jaakko', 'score': 3})

    def test_save_with_invalid_score(self):
        self.score_service.save('jaakko', 0)

        self.score_repository.save.assert_not_called()
