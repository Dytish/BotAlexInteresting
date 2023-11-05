from datetime import datetime
import dateutil.parser
from datetime import timedelta
from typing import Any
class Image:
    """
        Модель для таблицы Image
    """
    id: int
    url: str
    id_from_tg: str
    quest_id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime and int
    arrAttr: list = [ "url", "quest_id", "created_at", "updated_at", "deleted_at"]

    def __init__(self, 
                url: str = None, 
                id_from_tg: int = None, quest_id: int = None,
                 deleted_at: datetime and int = None) -> None :
        """
        Конструктор
        """
        self.url = url
        self.id_from_tg = id_from_tg
        self.quest_id = quest_id
        self.updated_at = datetime.now()
        if deleted_at == None:
            self.deleted_at = 0

    def __setattr__(self, __name: str, __value: Any) -> None:
        """
        надо переопределить, чтобы была проверка на тип данных
        конкретно в подписке
        """
        
        if (__name == "created_at") or (__name == "deleted_at"): 
            if type(__value) == str:
                __value = dateutil.parser.isoparse(__value)
        object.__setattr__(self, __name, __value)

    def newQuest(self) -> None :
        """
        При создании нового медиа
        """
        self.created_at = self.updated_at

    def delQuest(self) -> None :
        """
        При удалении медиа
        """
        self.deleted_at = datetime.now()