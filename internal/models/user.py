from datetime import datetime
class User:
    """
        Модель для таблицы users
    """
    id: int
    id_telegram: int
    username: str
    first_name: str
    last_name: str
    bio: str
    language_code: str
    utm: str
    status: str
    is_premium: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    type_user: int
    def __init__(self, id_telegram: int =None, username: str = None,
                first_name: str = None, last_name: str = None,
                bio: str = None, language_code: str = None,
                utm: str = None, status: str = None,
                is_premium: bool = None, deleted_at: datetime = None) -> None :
        """
        Конструктор 
        """
        self.id_telegram = id_telegram
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.bio = bio
        self.language_code = language_code
        self.utm = self.useUTM(utm)
        self.status = status
        self.is_premium = self.useIsPremium(is_premium) 
        self.updated_at = datetime.now()
        self.deleted_at = deleted_at

    def useIsPremium(self, is_premium: None or bool) -> bool:
        """Проверяет наличие премиум статуса"""
        if is_premium == None:
            is_premium = False
        return is_premium

    def useUTM(self, utm:str) -> None or str:
        """Проверяет наличие UTM метки"""
        if utm == None:
            return utm
        if utm.find('/start ') == -1:
            utm = None
        else:
            utm = utm.replace('/start ', '')
        return utm

    def newUser(self) -> None :
        """Определяет время создания для бд"""
        self.created_at = datetime.now()
        self.type_user = 1

    def delUser(self) -> None :
        """Определяет время удаления для бд"""
        self.deleted_at = datetime.now()