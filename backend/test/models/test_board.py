import unittest

from models.board_size import BoardSize
from models.board import Board

from ..fixtures.board import load_board_fixture

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = load_board_fixture()

    def test_columns(self):
        self.assertEqual(self.board.columns(), 7)

    def test_row(self):
        self.assertEqual(self.board.rows(), 6)

    def test_get_square(self):
        sq = self.board.get_square(2, 2)
        self.assertEqual(sq.player, 'player1')
        self.assertEqual(sq.available, False)

        sq = self.board.get_square(0, 4)
        self.assertEqual(sq.player, None)
        self.assertEqual(sq.available, True)

        sq = self.board.get_square(4, 1)
        self.assertEqual(sq.player, None)
        self.assertEqual(sq.available, False)

    def test_get_free_squares(self):
        fs = self.board.get_free_squares()

        coords = [sq.xy_coordinates() for sq in fs]
        self.assertEqual(coords, [(4, 0), (5, 0), (0, 3), (1, 3), (2, 3), (3, 3), (6, 3)])

        no_player = all(sq.player == None for sq in fs)
        self.assertTrue(no_player)

        no_available = all(sq.available == True for sq in fs)
        self.assertTrue(no_available)

class TestBoard_occupy_square(unittest.TestCase):
    def setUp(self):
        self.board = load_board_fixture('FullColumns')

    def subject(self, row, col):
        sq = self.board.get_square(row, col)
        return self.board.occupy_square(sq, 'player1')

    def test_ok_not_full_column(self):
        res = self.subject(3, 0)
        self.assertEqual(res.col, 0)
        self.assertEqual(res.row, 3)
        self.assertEqual(res.player, 'player1')
        self.assertEqual(res.available, False)

        self.assertEqual(self.board.num_free_squares, 7)
        sq = self.board.get_square(4, 0)
        self.assertEqual(sq.available, True)

    def test_ok_full_column(self):
        res = self.subject(5, 2)
        self.assertEqual(res.col, 2)
        self.assertEqual(res.row, 5)
        self.assertEqual(res.player, 'player1')
        self.assertEqual(res.available, False)

        self.assertEqual(self.board.num_free_squares, 6)

    def test_ko_already_occupied(self):
        with self.assertRaises(ValueError) as err:
            self.subject(1, 1)
        self.assertEqual(str(err.exception), "Already occupied")

    def test_ko_not_available(self):
        with self.assertRaises(ValueError) as err:
            self.subject(2, 4)
        self.assertEqual(str(err.exception), "Not available")

class TestBoard_get_combinations(unittest.TestCase):
    def setUp(self):
        board_size = BoardSize(6, 7)
        self.board = Board(board_size)
        self.comb_size = 4

    def combinations_to_tuples(self, combs):
        res = []
        for comb in combs:
            tups = [(sq.row, sq.col) for sq in comb]
            res.append(tups)
        return res

    def run_test(self, row, col, expected):
        combs = self.board.get_combinations(row, col, self.comb_size)
        tuples = self.combinations_to_tuples(combs)
        # lists order is not relevant in this test, probably not the best assertion
        # i dont wanna manually iterate/transform lists just to check unordered
        self.assertEqual(tuples, expected)

    def test_centered(self):
        [row, col] = [2, 3]
        expected = [
            [(2,0), (2,1), (2,2), (2,3)],
            [(2,1), (2,2), (2,3), (2,4)],
            [(2,2), (2,3), (2,4), (2,5)],
            [(2,3), (2,4), (2,5), (2,6)],
            [(0,3), (1,3), (2,3), (3,3)],
            [(1,3), (2,3), (3,3), (4,3)],
            [(2,3), (3,3), (4,3), (5,3)],
            [(0,1), (1,2), (2,3), (3,4)],
            [(1,2), (2,3), (3,4), (4,5)],
            [(2,3), (3,4), (4,5), (5,6)],
            [(0,5), (1,4), (2,3), (3,2)],
            [(1,4), (2,3), (3,2), (4,1)],
            [(2,3), (3,2), (4,1), (5,0)],
            
        ]
        self.run_test(row, col, expected)

    def test_00_corner(self):
        [row, col] = [0, 0]
        expected = [
            [(0,0), (0,1), (0,2), (0,3)],
            [(0,0), (1,0), (2,0), (3,0)],
            [(0,0), (1,1), (2,2), (3,3)],
        ]
        self.run_test(row, col, expected)

    def test_0max_corner(self):
        [row, col] = [0, 6]
        expected = [
            [(0,3), (0,4), (0,5), (0,6)],
            [(0,6), (1,6), (2,6), (3,6)],
            [(0,6), (1,5), (2,4), (3,3)],
        ]
        self.run_test(row, col, expected)

    def test_max0_corner(self):
        [row, col] = [5, 0]
        expected = [
            [(5,0), (5,1), (5,2), (5,3)],
            [(2,0), (3,0), (4,0), (5,0)],
            [(2,3), (3,2), (4,1), (5,0)],
        ]
        self.run_test(row, col, expected)

    def test_maxmax_corner(self):
        [row, col] = [5, 6]
        expected = [
            [(5,3), (5,4), (5,5), (5,6)],
            [(2,6), (3,6), (4,6), (5,6)],
            [(2,3), (3,4), (4,5), (5,6)],
        ]
        self.run_test(row, col, expected)

class TestBoard_get_square_error(unittest.TestCase):
    def test_error(self):
        board_size = BoardSize(6, 7)
        b = Board(board_size)
        with self.assertRaises(ValueError) as err:
            b.get_square(6, 1)
        self.assertEqual(str(err.exception), 'Invalid square position')