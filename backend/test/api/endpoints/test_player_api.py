from ...fixtures.api_test_framwork import ApiTestFramework
from ...fixtures.mocks import MockPlayerRepository
from backend.api.endpoints.player_api import PlayerAPi

class TestPlayerApi(ApiTestFramework):
    def setUp(self):
        super().setUp()
        self.api = PlayerAPi(self.app, MockPlayerRepository())
        self.load_endpoints()

    def test_get_all(self):
        res = self.client.get('/players')
        self.assertEqual(res.status_code, 200)
        self.assertListEqual(
            res.json,
            [{'id': 1, 'key': 'player1', 'name': 'Player', 'type': 'human'}, {'id': 2, 'key': 'player2', 'name': 'Cpu', 'type': 'cpu'}]
        )

    def test_update_player(self):
        res = self.client.put('/players/1', json={"name": "Pau"})
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(
            res.json,
            {'id': 1, 'key': 'player1', 'name': 'Pau', 'type': 'human'}
        )