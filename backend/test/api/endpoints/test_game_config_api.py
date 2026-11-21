from ...fixtures.api_test_framwork import ApiTestFramework
from ...fixtures.mocks import MockGameConfigRepository
from backend.api.endpoints.game_config_api import GameConfigAPi

class TestGameConfigApi(ApiTestFramework):
    def setUp(self):
        super().setUp()
        self.api = GameConfigAPi(self.app, MockGameConfigRepository())
        self.load_endpoints()

    def test_get_locale(self):
        res = self.client.get('/locale')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.json,
            { 'locale': 'es' }
        )

    def test_update_locale(self):
        res = self.client.put('/locale', json={"locale": "en"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.json,
            { 'locale': 'en' }
        )