import unittest

from services.move_tester import MoveTester
from ..fixtures.board import load_board_fixture

class TestMoveTester(unittest.TestCase):
    def setUp(self):
        self.board = load_board_fixture()

    def run_case(self, tc):
        square = self.board.get_square(tc['square'][0], tc['square'][1])
        comb = [self.board.get_square(pos[0], pos[1]) for pos in tc['combination']]

        self.assertTrue(
            MoveTester.is_all_player(tc['player'], square, comb),
            f"""Failed test case {tc}"""
        )

    def test_moves(self):
        test_cases = [
            {"player": "player1", "square": (3, 0), "combination": [(0, 0), (1, 0), (2, 0)]},
            {"player": "player1", "square": (3, 3), "combination": [(0, 0), (1, 1), (2, 2)]},
            {"player": "player2", "square": (3, 4), "combination": [(0, 1), (1, 2), (2, 3)]},
            {"player": "player1", "square": (0, 4), "combination": [(0, 2), (0, 3)]},
            {"player": "player2", "square": (1, 4), "combination": [(1, 2), (1, 3)]},
        ]
        for tc in test_cases:
            self.run_case(tc)