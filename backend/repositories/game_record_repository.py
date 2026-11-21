
from backend.models.game_record import GameRecord
from backend.repositories.base_repository import BaseRepository

class GameRecordRepository(BaseRepository):
    DEFAULT_PAGE_SIZE = 100
    MODEL = GameRecord

    def exists(self, hash_id: str):
        return self.__get_one_by_filter__(self.MODEL, self.MODEL.hash_id==hash_id) is not None

    def insert(self, game_record: MODEL):
        return self.__insert__(self.MODEL, game_record)

    def get_list(self, filter = None, page_size = DEFAULT_PAGE_SIZE):
        return self.__get_all__(self.MODEL, filter, 'id', page_size)



