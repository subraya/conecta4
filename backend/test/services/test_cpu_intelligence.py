import unittest

from models.game import Game
from models.rules import Rules
from services.cpu_intelligence import CpuIntelligence
from ..fixtures.game import load_game_fixture
from ..fixtures import difficulty_level

class TestCpuIntelligence_SuggestMoves(unittest.TestCase):
    def setUp(self):
        self.game = load_game_fixture()

    def suggest_move_tuples(self, player, difficulty):
        self.game.current_player = player
        cpu = CpuIntelligence(difficulty)
        squares = cpu.suggest_moves(self.game)
        return [(sq.row, sq.col) for sq in squares]

    def test_winner_moves(self):
        dl = difficulty_level.MOCK_WIN

        res = self.suggest_move_tuples('player1', dl)
        self.assertEqual(res, [(3, 0), (3, 3)])

        res = self.suggest_move_tuples('player2', dl)
        self.assertEqual(res, [(0, 4), (0, 5), (3, 0), (3, 1), (3, 2), (3, 3), (3, 6)])

    def test_win_blocker_moves(self):
        dl = difficulty_level.MOCK_BLOCK_WIN

        res = self.suggest_move_tuples('player1', dl)
        self.assertEqual(res, [(0, 4), (0, 5), (3, 0), (3, 1), (3, 2), (3, 3), (3, 6)])

        res = self.suggest_move_tuples('player2', dl)
        self.assertEqual(res, [(3, 0), (3, 3)])

    def test_uno_moves(self):
        dl = difficulty_level.MOCK_UNO

        res = self.suggest_move_tuples('player1', dl)
        self.assertEqual(res, [(0, 4), (3, 0), (3, 3)])

        res = self.suggest_move_tuples('player2', dl)
        self.assertEqual(res, [(3, 0), (3, 3)])

    def test_uno_blocker_moves(self):
        dl = difficulty_level.MOCK_BLOCK_UNO

        res = self.suggest_move_tuples('player1', dl)
        self.assertEqual(res, [(3, 0), (3, 3)])

        res = self.suggest_move_tuples('player2', dl)
        self.assertEqual(res, [(0, 4), (3, 0), (3, 3)])