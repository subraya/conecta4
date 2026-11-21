from .board import load_board_fixture

from models.rules import Rules
from models.game import Game

def load_game_fixture(fixture_name = 'Base'):
    board = load_board_fixture(fixture_name)
    game = Game(Rules(board.rows(), board.columns(), 4))
    game.board = board
    return game