
from repositories.game_record_repository import GameRecordRepository
from ..fixtures.db_test_framework import DBTestFramework
from models.game_record import GameRecord

SUT = GameRecordRepository()

class TestGameRecordRepository_exists(DBTestFramework):

    def subject(self, hash_id):
        return SUT.exists(hash_id)

    def test_subject(self):
        self.create_game_record(hash_id="hash-id")

        res = self.subject("hash-id")
        self.assertEqual(res, True)

        res = self.subject("another-hash-id")
        self.assertEqual(res, False)

class TestGameRecordRepository_insert(DBTestFramework):

    def subject(self, game_record):
        return SUT.insert(game_record)

    def test_subject(self):
        gr = GameRecord("player1", "cpu", "cpu", "normal", {}, [])

        res = self.subject(gr)
        self.assertIsNotNone(res)
        self.assertIsNotNone(res.id)

class TestGameRecordRepository_get_list(DBTestFramework):

    def subject(self, filter, page_size):
        return SUT.get_list(filter, page_size)

    def test_subject(self):
        self.create_game_record(hash_id="hash-id1")
        self.create_game_record(hash_id="hash-id2")
        self.create_game_record(hash_id="hash-id3")
        self.create_game_record(hash_id="hash-id4")
        self.create_game_record(hash_id="hash-id5")

        res = self.subject(None, 2)
        self.assertEqual(len(res), 2)
        self.assertListEqual([gr.hash_id for gr in res], ["hash-id1", "hash-id2"])

        res = self.subject(f'id > {res[-1].id}', 2)
        self.assertEqual(len(res), 2)
        self.assertListEqual([gr.hash_id for gr in res], ["hash-id3", "hash-id4"])

        res = self.subject(f'id > {res[-1].id}', 2)
        self.assertEqual(len(res), 1)
        self.assertListEqual([gr.hash_id for gr in res], ["hash-id5"])

        res = self.subject(f'id > {res[-1].id}', 2)
        self.assertEqual(len(res), 0)
