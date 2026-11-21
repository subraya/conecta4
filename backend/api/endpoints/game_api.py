import sys
from flask import request
from .. import responses, validations


class GameAPi():
    def __init__(self, app, player_repository, game_server, validations = {}):
        self.app = app
        self.player_repository = player_repository
        self.game_server = game_server
        self.validations = validations

    def load_endpoints(self):
        app = self.app

        @app.post('/games')
        def new_game():
            game_id = self.game_server.start_game()
            return ({"game_id": game_id})

        @app.get('/games/<game_id>/current_turn')
        def get_current_turn(game_id = None):
            ct = self.game_server.get_current_turn(game_id)
            return responses.CurrentTurnResponse(ct["player"], ct["free_squares"]).as_json()

        @app.get('/games/<game_id>/cpu_move')
        def get_cpu_move(game_id = None):
            # this endpoint can also be used to suggest moves to human players
            square = self.game_server.get_cpu_move(game_id)
            return responses.CpuMoveResponse(square, game_id).as_json()


        @app.post('/games/<game_id>/move')
        def move(game_id: str):
            move = request.json
            # inject validations via dependency to allow mock testing
            if not self.validations["player_exists"](move.get("player_id"), self.player_repository):
                return responses.InvalidPlayerResponse

            res = self.game_server.move(game_id, move.get("row"), move.get("col"), move.get("player_id"))
            ct = self.game_server.get_current_turn(game_id)

            return responses.PlayMoveResponse(ct, res).as_json()
