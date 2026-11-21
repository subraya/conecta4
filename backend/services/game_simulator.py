from .cpu_intelligence import CpuIntelligence
from models.game import Game
from models.game_record import GameRecord


class GameSimulator:
    def __init__(self, cpu: CpuIntelligence):
        self.cpu = cpu

    def simulate_game(self, rules):
        game = Game(rules)
        while not game.is_finished():
            move = self.cpu.get_move(game)
            game.move(move.row, move.col, game.current_player)

        return GameRecord(
            game.result,
            "cpu",
            "cpu",
            self.cpu.difficulty_level.key,
            game.rules.as_dict(),
            game.move_history
        )
    