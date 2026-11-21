# a file for each mocked class?
# a dedicated folder?

from models.player import Player
from models.square import Square

class MockCpu():
    def get_move(self, game):
        return 'mock cpu move'


class MockGame():
    def __init__(self):
        self.finished = False

    def is_finished(self):
        return self.finished

    def winner_info(self):
        return 'mock winner info'

    def current_turn_info(self):
        return 'mock current turn info'

    def move(self, row, col, player_key):
        return True

class MockPlayerRepository():
    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()
        self.p1.__dict__ = {"id": 1, "key": "player1", "name": "Player", "type": "human"}
        self.p2.__dict__ = {"id": 2, "key": "player2", "name": "Cpu", "type": "cpu"}
        self.err = None

    def get_all(self):
        return [self.p1, self.p2]

    def get_one_by_key(self, key):
        return self.p1 if key==self.p1.key else self.p2

    def update_player(self, id: int, props: dict):
        if self.err: return self.err
        p_ref = self.p1 if int(id)==self.p1.id else self.p2
        p = Player()
        p.__dict__ = p_ref.__dict__ | props
        return p

class MockGameConfigRepository():
    def __init__(self):
        self.locale = 'es'
        self.err = None

    def get_locale(self):
        return self.locale

    def update_locale(self, new_loc):
        if self.err: return self.err
        self.locale = new_loc
        return new_loc

class MockGameServer():
    def __init__(self):
        self.err = None

    def get_locale(self):
        return self.locale

    def update_locale(self, new_loc):
        if self.err: return self.err
        self.locale = new_loc
        return new_loc

    def start_game(self):
        return 'new_game_id'

    def get_current_turn(self, game_id):
        return {'player': 'player1', 'free_squares': []}

    def move(self, game_id, row, col, player):
        return {}

    def get_cpu_move(self, game_id):
        return Square(1,1)

class MockValidationPlayerExists():
    def __init__(self, b):
        self.val = b

    def run(self, player: str, repository):
        return self.val

