from ...fixtures.api_test_framwork import ApiTestFramework
from ...fixtures.mocks import MockPlayerRepository, MockGameServer, MockValidationPlayerExists
from backend.api.endpoints.game_api import GameAPi

class TestGameApi(ApiTestFramework):
    def setUp(self):
        super().setUp()
        self.validatiors = {
            "player_exists": MockValidationPlayerExists(True)
        }
        self.api = GameAPi(self.app, MockPlayerRepository(), MockGameServer(), {"player_exists": self.validatiors["player_exists"].run})
        self.load_endpoints()

    def test_new_game(self):
        res = self.client.post('/games')
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(
            res.json,
            ({"game_id": 'new_game_id'})
        )

    def test_get_current_turn(self):
        res = self.client.get('/games/1/current_turn')
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(
            res.json,
            {'current_player': 'player1', 'free_squares': []}
        )

    def test_move(self):
        res = self.client.post('/games/1/move', json={'row': 1, 'col': 1, 'player': 'player1'})
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(
            res.json,
            {'current_player': 'player1', 'free_squares': [], 'winner': None, 'winner_combination': None}
        )

    def test_cpu_move(self):
        res = self.client.get('/games/1/cpu_move')
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(
            res.json,
            {'game_id': '1', 'square': [1, 1]}
        )