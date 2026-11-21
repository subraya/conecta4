import unittest

from models.board_size import BoardSize

class TestBoardSize(unittest.TestCase):
    def test_is_valid_position(self):
        bs = BoardSize(6, 7)

        self.assertTrue(bs.is_valid_position(0, 0))
        self.assertTrue(bs.is_valid_position(5, 0))
        self.assertTrue(bs.is_valid_position(0, 6))
        self.assertTrue(bs.is_valid_position(5, 6))
        self.assertTrue(bs.is_valid_position(2, 3))

        self.assertFalse(bs.is_valid_position(-1, 3))
        self.assertFalse(bs.is_valid_position(6, 3))
        self.assertFalse(bs.is_valid_position(3, -1))
        self.assertFalse(bs.is_valid_position(3, 7))