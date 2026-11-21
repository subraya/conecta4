
import unittest

from models.square import Square

class TestSquare_occupy(unittest.TestCase):
    def setUp(self):
        self.square = Square(1,1)
        self.square.available = True

    def subject(self, *args):
        self.square.occupy(*args)

    def test_ok(self):
        self.assertEqual(self.square.player, None)
        self.assertEqual(self.square.available, True)

        self.subject("player1")
        self.assertEqual(self.square.player, 'player1')
        self.assertEqual(self.square.available, False)

    def test_ko_already_occupied(self):
        self.subject("player1")

        with self.assertRaises(ValueError) as err:
            self.subject("player2")
        self.assertEqual(str(err.exception), "Already occupied")

    def test_ko_not_availabke(self):
        self.square.available = False

        with self.assertRaises(ValueError) as err:
            self.subject("player1")
        self.assertEqual(str(err.exception), "Not available")


class TestSquare_mark_available(unittest.TestCase):
    def setUp(self):
        self.square = Square(1,1)

    def subject(self, *args):
        self.square.mark_available(*args)

    def test_ok(self):
        self.assertEqual(self.square.available, False)

        self.subject()
        self.assertEqual(self.square.available, True)

    def test_ko(self):
        self.square.player = "player1"
        with self.assertRaises(ValueError) as err:
            self.subject()
        self.assertEqual(str(err.exception), "Already occupied")

class TestSquare_coordinates(unittest.TestCase):
    def setUp(self):
        self.square = Square(4,2)

    def test_rowcol_coordinates(self):
        self.assertEqual(self.square.rowcol_coordinates(), (4, 2))

    def test_xy_coordinates(self):
        self.assertEqual(self.square.xy_coordinates(), (2, 4))