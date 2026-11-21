from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column
Base = declarative_base()

class GameConfig(Base):
    __tablename__ = "options"
    id = Column(Integer, primary_key=True)
    locale = Column(String)
    difficulty_level = Column(String)