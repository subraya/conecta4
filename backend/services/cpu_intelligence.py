import random
from backend.services.move_tester import MoveTester

class CpuIntelligence:
    def __init__(self, difficulty_level):
        self.difficulty_level = difficulty_level

    def get_move(self, game):
        # return one suggested move at random
        # the same move might be suggested multiple times
        # I'll assume this as a higher probability of being picked
        return random.choice(self.suggest_moves(game))

    def suggest_moves(self, game):
        moves = self.__get_winner_moves__(game)
        move_type = "winner"

        if not moves:
            moves = self.__get_win_blocking_moves__(game)
            move_type = "win_blocking"
        if not moves:
            moves = self.__get_uno_moves__(game)
            move_type = "uno"
        if not moves:
            moves = self.__get_uno_blocking_moves__(game)
            move_type = "uno_blocking"
        #if not decision:
        #    decision = self.get_uno_move()
        if not moves:
            # should this be here or as a part of get_move with a conditional on empty array?
            moves = game.board.get_free_squares()
            move_type = "random"
        #print(move_type)
        return moves

    def __get_winner_moves__(self, game):
        length = game.rules.goal
        prob = self.difficulty_level.prob_win
        player = game.current_player
        return self.__get_possible_moves_for_combination_length__(game, player, length, prob)

    def __get_win_blocking_moves__(self, game):
        length = game.rules.goal
        prob = self.difficulty_level.prob_block_win
        player = game.opponent_player()
        return self.__get_possible_moves_for_combination_length__(game, player, length, prob)

    def __get_uno_moves__(self, game):
        # TODO: FIX: move can be classified as uno even if the winning move is out of the board's bounds
        length = game.rules.goal - 1
        prob = self.difficulty_level.prob_uno
        player = game.current_player
        return self.__get_possible_moves_for_combination_length__(game, player, length, prob)
    
    def __get_uno_blocking_moves__(self, game):
        length = game.rules.goal - 1
        prob = self.difficulty_level.prob_block_uno
        player = game.opponent_player()
        return self.__get_possible_moves_for_combination_length__(game, player, length, prob)
        

    def __get_possible_moves_for_combination_length__(self, game, player, comb_length, detection_prob):
        free_squares = game.board.get_free_squares()
        moves = []
        for fs in free_squares:
            combs = game.board.get_combinations(fs.row, fs.col, comb_length)
            for comb in combs:
                # difficulty levels with prob < 1  adds a random chance of Cpu not detecting a good move
                if MoveTester.is_all_player(player, fs, comb) and self.__must_detect_move__(detection_prob):
                    moves.append(fs)
        return moves

    def __must_detect_move__(self, detection_prob):
        x = random.random()
        return x <= detection_prob

