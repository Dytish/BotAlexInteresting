from internal.models.user import User
from internal.database import user as dbUser
from internal.app.user import user as app_user
from aiogram import types

# def dbUser(*args) - > tuple:
#     return args
# -> Questionnaire
def isUser(user: User) ->int:
    """
       Проверяет есть ли такой пользователь в бд, 
        если есть изменяет статус
        Возвращает тип пользоватеня
    """
    # print(user.__dict__)
    if (dbUser.check(user.id_telegram) == 0):
        user.newUser()
        user_tuple = user.__dict__
        user_tuple = tuple(user_tuple.values())
        dbUser.add_new(user_tuple)
        del user_tuple
    else:
        user_tuple = (user.status, user.updated_at, user.id_telegram)
        dbUser.change_status(user_tuple)
    return  dbUser.take_type_user(user.id_telegram)
        
def isAdmin(id_telegram: int) -> types.ReplyKeyboardMarkup:
    """Определяет тип пользователя """
    take_type_user = dbUser.take_type_user(id_telegram)
    if take_type_user == 2:
        return True
    else: 
        return False
    

def typeСhecking(id_telegram: int) -> types.ReplyKeyboardMarkup:
    """Определяет тип пользователя и какуюклавиатуру откпарвить"""
    take_type_user = dbUser.take_type_user(id_telegram)
    print(take_type_user)
    if isAdmin(id_telegram):
        return app_user.keyboard_user_admin(id_telegram) 
    else:
        return app_user.keyboard_user_user
        # print("sd", user.__dict__)
        # print("sd", user_tuple)
        # del dict_sample["year"] 
        

# def isIdTelegram(string:str) -> bool:
#     return len(string) < 50

def isUsername(string:str) -> bool:
    return len(string) < 100

def isFirstName(string:str) -> bool:
    return len(string) < 100

def isLastName(string:str) -> bool:
    return len(string) < 100

def isBio(string:str) -> bool:
    return len(string) < 70

def isLanguageCode(string:str) -> bool:
    return len(string) < 50

def isUtm(string:str) -> bool:
    return len(string) < 100

def isPremium(string:str) -> bool:
    return len(string) < 200