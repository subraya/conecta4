import unittest

from api.app import create_app

class ApiTestFramework(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.api = None
        self.loaded = False

    def load_endpoints(self):
        if self.loaded: return
        self.api.load_endpoints()
        self.loaded = True

    def tearDown(self):
        #remove endpoints
        pass
