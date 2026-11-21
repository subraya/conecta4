
from flask import request

class GameConfigAPi():
    def __init__(self, app, game_config_repository, validations = {}):
        self.app = app
        self.game_config_repository = game_config_repository
        self.validations = validations

    def load_endpoints(self):
        app = self.app

        @app.get('/locale')
        def get_locale():
            return {"locale": self.game_config_repository.get_locale()}

        @app.put('/locale')
        def save_locale():
            params = request.json
            updated_locale = self.game_config_repository.update_locale(params.get("locale"))
            return {"locale": updated_locale}
