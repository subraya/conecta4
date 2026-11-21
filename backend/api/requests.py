from pydantic import BaseModel

class NewGameRules(BaseModel):
  rows: int
  columns: int
  goal: int

class PlayerMove(BaseModel):
  game_id: str
  row: int
  col: int
  player_id: str