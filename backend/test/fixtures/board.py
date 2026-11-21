import sys
sys.path.append("..")
from models.board import Board
from models.board_size import BoardSize

FIXTURES = {
    'Base': [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 2, 1, 2, 0, 0, 1],
        [1, 1, 2, 2, 0, 0, 2],
        [1, 2, 1, 1, 0, 0, 2],
    ],
    'FullColumns': [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 0],
        [1, 2, 1, 2, 0, 0, 1],
        [1, 1, 2, 2, 0, 0, 2],
        [1, 2, 1, 1, 0, 0, 2],
    ],
    'Draw': [
        [2, 0, 1, 2, 2, 1, 1],
        [2, 2, 1, 1, 2, 2, 1],
        [1, 1, 2, 2, 1, 1, 2],
        [2, 2, 1, 1, 2, 2, 1],
        [1, 1, 2, 2, 1, 1, 2],
        [1, 1, 2, 2, 1, 1, 2],
    ]
}

def load_board_fixture(fixture_name = 'Base'):
    fixt = FIXTURES[fixture_name]
    rows = len(fixt)
    cols = len(fixt[0])
    bs = BoardSize(rows, cols)
    board = Board(bs)

    for r_idx in reversed(range(rows)):
        for c_idx in range(cols):
            player = fixt[r_idx][c_idx]
            if player != 0:
                player_key = "player1" if player == 1 else "player2"
                sq = board.get_square(rows - 1 - r_idx, c_idx)
                board.occupy_square(sq, player_key)
    return board