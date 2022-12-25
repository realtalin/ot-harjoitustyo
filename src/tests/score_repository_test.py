import unittest
from repositories.score_repository import score_repository


class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        score_repository.delete_all()
        self.score_jaakko_3 = {'username': 'jaakko', 'score': 3}
        self.score_markku_5 = {'username': 'markku', 'score': 5}

    def test_save(self):
        score_repository.save(self.score_jaakko_3)

        scores = score_repository.fetch_all()

        self.assertEqual(len(scores), 1)
        self.assertEqual(scores[0]['username'], 'jaakko')
        self.assertEqual(scores[0]['score'], 3)

    def test_fetch_all(self):
        score_repository.save(self.score_jaakko_3)
        score_repository.save(self.score_markku_5)

        scores = score_repository.fetch_all()

        self.assertEqual(len(scores), 2)
        self.assertEqual(scores[0]['username'], 'jaakko')
        self.assertEqual(scores[0]['score'], 3)
        self.assertEqual(scores[1]['username'], 'markku')
        self.assertEqual(scores[1]['score'], 5)

    def test_delete_all(self):
        score_repository.save(self.score_jaakko_3)
        score_repository.delete_all()

        scores = score_repository.fetch_all()

        self.assertEqual(len(scores), 0)
