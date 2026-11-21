#I guess different api frameworks have built-in libraries to do this, but I'm not doing the research now

class JsonResponse:
    def as_json(self):
        return self.__dict__

class PlayerResponse(JsonResponse):
    def __init__(self, player):
        self.id = player.id
        self.key = player.key
        self.name = player.name
        self.type = player.type

class CurrentTurnResponse(JsonResponse):
    def __init__(self, player_key, free_squares):
        self.current_player = player_key
        self.free_squares = [fs.xy_coordinates() for fs in free_squares]

class SimulatedGame(JsonResponse):
    def __init__(self, winner, moves, winner_combination):
        self.winner = winner
        self.moves = moves
        self.winner_combination = winner_combination


class PlayMoveResponse(JsonResponse):
    def __init__(self, next_turn_info: dict, endgame_info: dict):
        self.winner = endgame_info.get("winner")
        self.winner_combination = endgame_info.get("winner_combination")
        if self.winner_combination:
            self.winner_combination = [sq.xy_coordinates() for sq in self.winner_combination]
        self.current_player = next_turn_info["player"]
        self.free_squares = [fs.xy_coordinates() for fs in next_turn_info["free_squares"]]

class CpuMoveResponse(JsonResponse):
    def __init__(self, square, game_id):
        self.square = square.xy_coordinates()
        self.game_id = game_id

InvalidPlayerResponse = ("Invalid player", 400)