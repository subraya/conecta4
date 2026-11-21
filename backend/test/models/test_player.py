
import sqlalchemy
from ..fixtures.db_test_framework import DBTestFramework

class TestPlayer_unique_key(DBTestFramework):

    def test_uniqueness_error(self):
        self.create_player('player1')

        with self.assertRaises(sqlalchemy.exc.IntegrityError) as err:
            self.create_player('player1')
