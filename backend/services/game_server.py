
from backend.models.game import Game
from backend.models import rules
from backend.services.cpu_intelligence import CpuIntelligence
import uuid

class GameServer:
    def __init__(self, cpu: CpuIntelligence):
        self.games = {}
        self.cpu = cpu

    def start_game(self):
        game_id = str(uuid.uuid4())
        self.games[game_id] = Game(rules.DEFAULT)
        return game_id

    def get_current_turn(self, game_id):
        return self.games[game_id].current_turn_info()

    def move(self, game_id: str, row: int, col: int, player_key: str):
        game = self.games[game_id]
        game.move(row, col, player_key)
        if game.is_finished():
            return game.winner_info()
        else:
            return {}

    def get_cpu_move(self, game_id: str):
        return self.cpu.get_move(self.games[game_id])

