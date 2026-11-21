
from flask import request
from .. import responses


class PlayerAPi():
    def __init__(self, app, player_repository, validations={}):
        self.app = app
        self.player_repository = player_repository
        self.validations = validations

    def load_endpoints(self):
        app = self.app

        @app.get('/players')
        def get_players():
            players = self.player_repository.get_all()
            return [responses.PlayerResponse(p).as_json() for p in players]

        @app.put('/players/<id>')
        def update_player(id: int):
            params = request.json
            updated_player = self.player_repository.update_player(id, params)
            return responses.PlayerResponse(updated_player).as_json()

