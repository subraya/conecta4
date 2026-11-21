from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column
Base = declarative_base()

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True)
    name = Column(String)
    type = Column(String)

    """
    def __init__(self, player_key):
        self.__validate__(player_key)
        self.key = player_key

    def opponent_key(self):
        if self.key == "Player1":
            return "Player2"
        return "Player1"

    def __validate__(self, player_key):
        if player_key not in self.VALID_KEYS:
            raise ValueError("Invalid player key. Allowed values: " + str(self.VALID_KEYS))
    """