from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Float, Column
Base = declarative_base()

class DifficultyLevel(Base):
    __tablename__ = "difficulty_levels"
    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True)
    rank = Column(Integer, unique=True)
    prob_win = Column(Float)
    prob_block_win = Column(Float)
    prob_uno = Column(Float)
    prob_block_uno = Column(Float)
    prob_majority = Column(Float)
    prob_block_majority = Column(Float)
