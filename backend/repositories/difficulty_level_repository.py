
from backend.models.difficulty_level import DifficultyLevel
from backend.repositories.base_repository import BaseRepository


class DifficultyLevelRepository(BaseRepository):
    MODEL = DifficultyLevel

    def get_one(self, key: str):
        return self.__get_one_by_filter__(self.MODEL, self.MODEL.key==key)
