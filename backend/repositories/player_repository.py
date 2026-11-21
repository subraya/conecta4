
from backend.models.player import Player
from backend.repositories.base_repository import BaseRepository


class PlayerRepository(BaseRepository):
    MODEL = Player

    def get_all(self):
        return self.__get_all__(self.MODEL)

    def update_player(self, id: int, props: dict):
        self.__update__(self.MODEL, id, props)
        return self.get_one(id)

    def get_one(self, id: int):
        return self.__get_one_by_filter__(self.MODEL, self.MODEL.id==id)

    def get_one_by_key(self, key: str):
        return self.__get_one_by_filter__(self.MODEL, self.MODEL.key==key)



