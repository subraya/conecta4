
from repositories.game_config_repository import GameConfigRepository
from ..fixtures.db_test_framework import DBTestFramework

SUT = GameConfigRepository()

class TestPlayerRespository_get_locale(DBTestFramework):

    def subject(self):
        return SUT.get_locale()

    def test_subject(self):
        self.create_game_config()

        res = self.subject()
        self.assertEqual(res, 'es')

class TestPlayerRespository_update_locale(DBTestFramework):

    def subject(self, locale: str):
        return SUT.update_locale(locale)

    def test_subject(self):
        gc = self.create_game_config()
        self.assertEqual(gc.locale, 'es')

        res = self.subject('ca')
        self.assertEqual(res, 'ca')

        loc = SUT.get_locale()
        self.assertEqual(loc, 'ca')

class TestPlayerRespository_get_difficulty_level(DBTestFramework):

    def subject(self):
        return SUT.get_difficulty_level()

    def test_subject(self):
        self.create_game_config()

        res = self.subject()
        self.assertEqual(res, 'normal')


