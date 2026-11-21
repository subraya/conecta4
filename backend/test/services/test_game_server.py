import unittest

from services.game_server import GameServer

from ..fixtures import mocks

class TestGameServer(unittest.TestCase):
    def setUp(self):
        self.game_server = GameServer(mocks.MockCpu())
        self.mock_game = mocks.MockGame()

    def test_start_game(self):
        self.game_server.start_game()
        self.assertEqual(len(self.game_server.games.items()), 1)

        from backend.models.game import Game
        self.assertIsInstance(list(self.game_server.games.values())[0], Game)

    def test_get_current_turn(self):
        self.game_server.games['game_id'] = self.mock_game
        res = self.game_server.get_current_turn('game_id')
        self.assertEqual(res, 'mock current turn info')

    def test_move(self):
        self.game_server.games['game_id'] = self.mock_game
        res = self.game_server.move('game_id', 1, 1, 'player1')
        self.assertEqual(res, {})

        self.mock_game.finished = True
        res = self.game_server.move('game_id', 1, 1, 'player1')
        self.assertEqual(res, 'mock winner info')

    def test_get_cpu_move(self):
        self.game_server.games['game_id'] = self.mock_game
        res = self.game_server.get_cpu_move('game_id')
        self.assertEqual(res, 'mock cpu move')