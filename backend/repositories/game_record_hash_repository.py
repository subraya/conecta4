
from backend.models.game_record_hash import GameRecordHash
from backend.repositories.base_repository import BaseRepository

class GameRecordHashRepository(BaseRepository):
    DEFAULT_PAGE_SIZE = 100
    MODEL = GameRecordHash

    def exists(self, hash_id: str):
        return self.__get_one_by_filter__(self.MODEL, self.MODEL.hash_id==hash_id) is not None

    def insert(self, record: MODEL):
        return self.__insert__(self.MODEL, record)




