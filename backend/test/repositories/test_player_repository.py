
from repositories.player_repository import PlayerRepository
from ..fixtures.db_test_framework import DBTestFramework

SUT = PlayerRepository()


class TestPlayerRespository_get_all(DBTestFramework):

    def subject(self):
        return SUT.get_all()

    def test_get_all(self):
        self.create_player('player1')
        self.create_player('player2')
        self.create_player('player3')

        res = self.subject()
        self.assertEqual(len(res), 3)
        self.assertCountEqual([p.key for p in res], ['player1', 'player2', 'player3'])

class TestPlayerRespository_get_one_by_key(DBTestFramework):

    def subject(self, key):
        return SUT.get_one_by_key(key)

    def test_subject(self):
        self.create_player('player1', name = 'Pau')

        res = self.subject('player2')
        self.assertIsNone(res)

        res = self.subject('player1')
        self.assertIsNotNone(res)
        self.assertEqual(res.name, 'Pau')

class TestPlayerRespository_get_one(DBTestFramework):

    def subject(self, id):
        return SUT.get_one(id)

    def test_subject(self):
        player = self.create_player('player1', type = 'CPU')

        res = self.subject(player.id+1)
        self.assertIsNone(res)

        res = self.subject(player.id)
        self.assertIsNotNone(res)
        self.assertEqual(res.type, 'CPU')

class TestPlayerRespository_update(DBTestFramework):

    def subject(self, id, changes):
        return SUT.update_player(id, changes)

    def test_subject(self):
        player = self.create_player('player1')

        res = self.subject(player.id, {"name": "Pau", "type": "CPU"})
        self.assertEqual(res.id, player.id)
        self.assertEqual(res.name, 'Pau')
        self.assertEqual(res.type, 'CPU')

        # looking at this, I'm not so sure anymore update implementation should internally return a get_one
        # for this particular application is irrelevant, but still
        res = SUT.get_one(player.id)
        self.assertEqual(res.id, player.id)
        self.assertEqual(res.name, 'Pau')
        self.assertEqual(res.type, 'CPU')