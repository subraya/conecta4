
from backend.models.game_config import GameConfig
from backend.repositories.base_repository import BaseRepository


class GameConfigRepository(BaseRepository):
    MODEL = GameConfig

    def get_locale(self):
        return self.__get_all__(self.MODEL)[0].locale

    def update_locale(self, locale: str):
        # this is a weird line between a normal realistic scenario and a totally contrived example
        # truth is, in this application, 'id' columns are really useless and 'key' are way more meaningful, I'm just using id 'cause tradition
        # here, I could totally use the fact there's only one row in the table (or one per profile at most)
        gc = self.__get_all__(self.MODEL)[0]
        self.__update__(self.MODEL, gc.id, {"locale": locale})
        return self.get_locale()

    def get_difficulty_level(self):
        return self.__get_all__(self.MODEL)[0].difficulty_level



