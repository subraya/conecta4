
from models.difficulty_level import DifficultyLevel

def mock_difficulty_level(prob_win, prob_block_win, prob_uno, prob_block_uno):
    dl = DifficultyLevel()
    dl.prob_win = prob_win
    dl.prob_block_win = prob_block_win
    dl.prob_uno = prob_uno
    dl.prob_block_uno = prob_block_uno
    return dl

MOCK_BASE = mock_difficulty_level(1, 1, 1, 1)
MOCK_WIN = mock_difficulty_level(1, 0, 0, 0)
MOCK_BLOCK_WIN = mock_difficulty_level(0, 1, 0, 0)
MOCK_UNO = mock_difficulty_level(0, 0, 1, 0)
MOCK_BLOCK_UNO = mock_difficulty_level(0, 0, 0, 1)