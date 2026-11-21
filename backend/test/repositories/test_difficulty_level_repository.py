
from repositories.difficulty_level_repository import DifficultyLevelRepository
from ..fixtures.db_test_framework import DBTestFramework

SUT = DifficultyLevelRepository()

class TestPlayerRespository_get_one(DBTestFramework):

    def subject(self, key):
        return SUT.get_one(key)

    def test_subject(self):
        self.create_difficulty_level()

        res = self.subject('easy')
        self.assertIsNone(res)

        res = self.subject('normal')
        self.assertIsNotNone(res)
        self.assertEqual(res.prob_win, 0.9)
