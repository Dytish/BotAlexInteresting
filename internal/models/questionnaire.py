from datetime import datetime
import dateutil.parser
from datetime import timedelta
from typing import Any
class Questionnaire:
    """
        Модель для таблицы questionnaires
    """
    id: int
    user_tg_id: int
    images: list
    title: str
    previe: str
    info: str
    info_mob: str
    info_social: dict
    vip: int
    sub: datetime
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime and int
    active: bool
    arrAttr: list = [ "images", "title", "previe", "info", "info_mob", "info_social", "vip", "sub"]

    def __init__(self, user_tg_id: int , images:list = None,
                title: str = None, previe: str = None,
                info: str = None, info_mob: str = None,
                info_social: dict = None, vip: int = None,
                sub:datetime = None, deleted_at: datetime and int = None, active: bool = None) -> None :
        """
        Конструктор
        """
        self.user_tg_id = user_tg_id
        if images == None:
            images = []
        self.images = images
        self.title = title
        self.previe = previe
        self.info = info
        self.info_mob = info_mob
        if info_social == None:
            info_social = {}
        if type(info_social) == str:
            self.info_social = info_social
        else:
            self.info_social = info_social
        if vip == None:
            vip = 10
        self.vip = vip
        if sub == None:
            sub = datetime.now() - timedelta(days=1)
        if type(sub) == str:
            self.sub = dateutil.parser.isoparse(sub)
        else:
            self.sub = sub 
        self.updated_at = datetime.now()
        if deleted_at == None:
            self.deleted_at = 0
        if active == None:
            self.active = False
    # def __getitem__(self, index):

    #     if index >= 5:
    #         raise IndexError('End')
    #     return "Hiii"

    def __setattr__(self, __name: str, __value: Any) -> None:
        """
        надо переопределить, чтобы была проверка на тип данных
        конкретно в подписке
        """
        if __name == "sub" and type(__value) == int:
            if self.sub > datetime.now():
                __value = self.sub + timedelta(days=__value)
            else:
                __value = datetime.now() + timedelta(days=__value)
        if (__name == "created_at") or (__name == "deleted_at"): 
            if type(__value) == str:
                __value = dateutil.parser.isoparse(__value)
        object.__setattr__(self, __name, __value)

    def newQuest(self) -> None :
        """
        При создании новой анкеты
        """
        self.created_at = self.updated_at

    def delQuest(self) -> None :
        """
        При удалении анкеты
        """
        self.deleted_at = datetime.now()

    def dict(self) -> dict:
        """
        переводит атрибуты в словарик
        """
        quesrDict = {}
        for key, value in self.__dict__.items():
            print(key, value)
            quesrDict[str(key)] = value
        return quesrDict