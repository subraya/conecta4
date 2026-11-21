import hashlib

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column
Base = declarative_base()

class GameRecordHash(Base):
    __tablename__ = "game_record_hashes"
    hash_id = Column(String, primary_key=True)
