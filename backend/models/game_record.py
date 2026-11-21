import hashlib

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.types import ARRAY
Base = declarative_base()

class GameRecord(Base):
    __tablename__ = "game_records"
    id = Column(Integer, primary_key=True)
    winner = Column(String)
    player1_type = Column(String)
    player2_type = Column(String)
    difficulty = Column(String)
    rules = Column(JSON)
    hash_id = Column(String)
    moves = Column(ARRAY(String))

    def __init__(self, winner, player1_type, player2_type, difficulty, rules, moves):
        self.winner = winner
        self.player1_type = player1_type
        self.player2_type = player2_type
        self.difficulty = difficulty
        self.rules = rules
        self.moves = moves
        self.hash_id = self.__generate_hash_id__()

    def __generate_hash_id__(self):
        comp = f"{self.winner}-{self.player1_type}-{self.player2_type}-{self.rules}-{self.moves}"
        return hashlib.sha256(comp.encode("utf-8")).hexdigest()