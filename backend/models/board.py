import itertools

from .board_size import BoardSize
from .square import Square

class Board:
    def __init__(self, board_size: BoardSize):
        self.board_size = board_size
        self.squares = self.__init_squares__()
        self.num_free_squares = len(self.get_free_squares())

    def rows(self):
        return self.board_size.rows

    def columns(self):
        return self.board_size.columns

    def get_square(self, row: int, col: int):
        if not self.board_size.is_valid_position(row, col):
            raise ValueError("Invalid square position")

        return self.squares[self.columns()*row + col]

    # TODO: get square, occupy square: validate the square and raise controlled exception if coords are out of bounds

    def occupy_square(self, square: Square, player_key: str):
        square.occupy(player_key)

        if square.row != self.board_size.rows - 1:
            self.get_square(square.row+1, square.col).mark_available()
        else:
            self.num_free_squares -= 1

        return square

    def get_free_squares(self):
        return list(filter(lambda sq: sq.available, self.squares))
    
    def get_combinations(self, row, col, comb_size):
        combinations = []
        combinations.append(self.__horizontal_combinations__(row, col, comb_size))
        combinations.append(self.__vertical_combinations__(row, col, comb_size))
        combinations.append(self.__diag1_combinations__(row, col, comb_size))
        combinations.append(self.__diag2_combinations__(row, col, comb_size))
        return list(itertools.chain(*combinations))

    def draw(self):
        table = ["\n"]
        for sq in self.squares:
            sq_val = "_"
            if sq.player == "player1":
                sq_val = "1"
            elif sq.player == "player2":
                sq_val = "2"
            table.append(sq_val)
            if sq.col == self.columns() - 1:
                table.append("\n")
        print(" ".join(table))

        
    def __init_squares__(self):
        squares = []
        for r in range(self.rows()):
            for c in range(self.columns()):
                sq = Square(r, c)
                if r == 0:
                    sq.mark_available()
                squares.append(sq)
        return squares

    def __horizontal_combinations__(self, row, col, comb_size):
        min_col = max(0, col - (comb_size-1))
        max_col = min(self.columns()-1, col + (comb_size-1))+1 #+1 to force the inclusive slicing
        squares = self.squares[
            self.columns()*row + min_col :
            self.columns()*row + max_col
        ]
        return self.__apply_comb_size_to_square_list__(squares, row, col, comb_size)

    def __vertical_combinations__(self, row, col, comb_size):
        min_row = max(0, row - (comb_size-1))
        max_row = min(self.rows()-1, row + (comb_size-1))
        squares = []
        for idx in range(min_row, max_row+1):
            squares.append(self.squares[self.columns()*idx + col])
        return self.__apply_comb_size_to_square_list__(squares, row, col, comb_size)

    def __diag1_combinations__(self, row, col, comb_size):
        squares = []
        for offset in range(-(comb_size-1), comb_size):
            r = row + offset
            c = col + offset
            if r >= 0 and c >= 0 and r < self.rows() and c < self.columns():
                sq = self.get_square(r, c)
                squares.append(sq)
        return self.__apply_comb_size_to_square_list__(squares, row, col, comb_size)

    def __diag2_combinations__(self, row, col, comb_size):
        squares = []
        for offset in range(-(comb_size-1), comb_size):
            r = row + offset
            c = col - offset
            if r >= 0 and c >= 0 and r < self.rows() and c < self.columns():
                sq = self.get_square(r, c)
                squares.append(sq)
        return self.__apply_comb_size_to_square_list__(squares, row, col, comb_size)

    def __apply_comb_size_to_square_list__(self, squares, row, col, comb_size):
        combs = []
        for idx in range(len(squares)-(comb_size-1)):
            subset = squares[idx:idx+comb_size]
            if len(subset)==comb_size and any(sq.col == col and sq.row == row for sq in subset):
                combs.append(subset)
        return combs