
from flask import Flask
from flask_cors import CORS

from .endpoints.game_api import GameAPi
from .endpoints.game_config_api import GameConfigAPi
from .endpoints.player_api import PlayerAPi
from .validations import validate_player_exists

from backend.repositories.player_repository import PlayerRepository
from backend.repositories.game_config_repository import GameConfigRepository
from backend.repositories.difficulty_level_repository import DifficultyLevelRepository

from backend.services.game_server import GameServer
from backend.services.cpu_intelligence import CpuIntelligence

PORT = 8000

def create_app():
    app = Flask(__name__)
    CORS(app)
    return app

def prepare_app(app):
    # not a fan of using global variables like this, but as long as it works in this dummy training project, I'll be fine with it

    # INJECTABLE DEPENDENCIES
    player_repository = PlayerRepository()
    game_config_repository = GameConfigRepository()
    difficulty_level_repository = DifficultyLevelRepository()

    cpu = CpuIntelligence(
        difficulty_level_repository.get_one(game_config_repository.get_difficulty_level())
    )
    game_server = GameServer(cpu)

    # LOAD ENDPOINTS FOR DIFFERENT RESOURCES
    PlayerAPi(app, player_repository).load_endpoints()
    GameConfigAPi(app, game_config_repository).load_endpoints()
    GameAPi(app, player_repository, game_server, {'player_exists': validate_player_exists}).load_endpoints()

if __name__ == "__main__":
    app = create_app()
    prepare_app(app)
    app.run(debug=True, port=PORT)
