
from .rules import Rules
from .board import Board

class Game:
    def __init__(self, rules: Rules):
        self.rules = rules
        self.result = None
        self.board = Board(rules.board_size)
        self.num_free_squares = len(self.get_free_squares())
        self.winner_combination = None
        self.current_player = "player1"
        self.move_history = []
        return None

    def opponent_player(self):
        if self.current_player == "player1":
            return "player2"
        return "player1"

    def current_turn_info(self):
        return {"player": self.current_player, "free_squares": self.get_free_squares()}

    def winner_info(self):
        return {"winner": self.result, "winner_combination": self.winner_combination}

    def is_finished(self):
        return (self.result is not None)

    def move(self, row: int, col: int, player_key: str):
        if player_key != self.current_player: raise ValueError("Not current player")

        square = self.board.get_square(row, col)
        self.board.occupy_square(square, player_key)
        self.move_history.append(square.as_move_str())
        self.__alternate_player__()

        if self.__is_winner_move__(square):
            self.__set_result__(player_key)
        elif self.board.num_free_squares == 0:
            self.__set_result__("draw")

    def get_free_squares(self):
        return self.board.get_free_squares()

    def __alternate_player__(self):
        if self.current_player == "player1":
            self.current_player = "player2"
        else:
            self.current_player = "player1"

    def __is_winner_move__(self, square):
        combs = self.board.get_combinations(square.row, square.col, self.rules.goal)
        for comb in combs:
            if all(square.player == sq.player for sq in comb):
                self.winner_combination = comb
                return True
        return False
            
    def __set_result__(self, result):
        if not self.result:
            self.result = result