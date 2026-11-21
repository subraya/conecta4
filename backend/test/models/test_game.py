import unittest

from models.game import Game

from ..fixtures.game import load_game_fixture

class TestGame_normal_move(unittest.TestCase):
    # every individual test method could be a subject on their own,
    # but given that I'm interested in testing how the game is updated when a player makes a move
    # I'm making move() the subject
    # number of times subject is executed VS short, focused, readable tests

    def setUp(self):
        self.game = load_game_fixture()

    def subject(self):
        self.game.move(0, 4, 'player1')

    def test_current_turn_info(self):
        ct = self.game.current_turn_info()
        self.assertEqual(ct["player"], "player1")
        self.assertEqual(ct["free_squares"], self.game.board.get_free_squares())

        self.subject()

        ct = self.game.current_turn_info()
        self.assertEqual(ct["player"], "player2")
        self.assertEqual(ct["free_squares"], self.game.board.get_free_squares())

    def test_opponent_player(self):
        op = self.game.opponent_player()
        self.assertEqual(op, "player2")

        self.subject()

        op = self.game.opponent_player()
        self.assertEqual(op, "player1")

    def test_is_finished(self):
        self.subject()
        self.assertEqual(self.game.is_finished(), False)

    def test_result_info(self):
        self.subject()
        win = self.game.winner_info()
        self.assertDictEqual(win, {"winner": None, "winner_combination": None})

class TestGame_winning_move(unittest.TestCase):
    def setUp(self):
        self.game = load_game_fixture()

    def subject(self):
        self.game.move(3, 0, 'player1')

    def test_is_finished(self):
        self.subject()
        self.assertEqual(self.game.is_finished(), True)

    def test_result_info(self):
        self.subject()
        win = self.game.winner_info()
        self.assertDictEqual(win, {
            "winner": 'player1', 
            "winner_combination": [self.game.board.get_square(0, 0), self.game.board.get_square(1, 0), self.game.board.get_square(2, 0), self.game.board.get_square(3, 0)]
        })

class TestGame_draw_game(unittest.TestCase):
    def setUp(self):
        self.game = load_game_fixture('Draw')
        self.game.current_player = 'player2'

    def subject(self):
        self.game.move(5, 1, 'player2')

    def test_is_finished(self):
        self.subject()
        self.assertEqual(self.game.is_finished(), True)

    def test_result_info(self):
        self.subject()
        win = self.game.winner_info()
        self.assertDictEqual(win, {
            "winner": 'draw', 
            "winner_combination": None
        })

class TestGame_invalid_moves(unittest.TestCase):

    def setUp(self):
        self.game = load_game_fixture()

    def test_not_current_player(self):
        with self.assertRaises(ValueError) as err:
            self.game.move(3, 0, "player2")
        self.assertEqual(str(err.exception), "Not current player")

    def test_already_occupied(self):
        with self.assertRaises(ValueError) as err:
            self.game.move(2, 0, "player1")
        self.assertEqual(str(err.exception), "Already occupied")

    def test_not_available(self):
        with self.assertRaises(ValueError) as err:
            self.game.move(4, 0, "player1")
        self.assertEqual(str(err.exception), "Not available")

    def test_square_not_exists(self):
        with self.assertRaises(ValueError) as err:
            self.game.move(6, 0, "player1")
        self.assertEqual(str(err.exception), "Invalid square position")
