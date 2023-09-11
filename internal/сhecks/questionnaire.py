from internal.models.questionnaire import Questionnaire
from internal.database import questionnaire as dbUQuest
import os
import json

def isQuestionnaire(data: dict, tg_id: int) -> Questionnaire:
    """
    Проверка есть ли уже в состоянии переменная questionnaire
    """
    try:
        questionnaire = data["questionnaire"]
    except KeyError:
        questionnaire = Questionnaire(user_tg_id=tg_id)
    print(questionnaire.__dict__)
    return questionnaire

def isMediaGroups(data: dict) -> dict:
    """
    Проверка есть ли уже в состоянии переменная media_groups
    """
    try:
        media_groups = data["media_groups"]
        return data
    except KeyError:
        data["media_groups"] = []
        return data
    

def isImages( questionnaire:Questionnaire, messages:dict) -> (Questionnaire, str):
    """
    Добавление и сохраниение медиа
    """
    if messages.photo:
        # print('foto')
        name = messages.photo[-1].file_unique_id + ".jpg"
    elif messages.video:
        # print('video')
        name = messages.video.file_unique_id + ".WEBM"
        # path = os.path.join(f"pkg/images/{name}")
    questionnaire.images.append(name)
    path = f"/pkg/images/{name}"
    return questionnaire, path

def isAVideo(path: str) -> bool:
    """
    Проверяет видео ли пытаются сохранить
    """
    extension_file = path.split(".")[-1]
    return extension_file == "WEBM"

def isTitle(string:str) -> bool:
    """
    Проверка длины строки
    """
    return len(string) < 50

def isPrevie(string:str) -> bool:
    """
    Проверка длины строки
    """
    return len(string) < 100

def isInfo(string:str) -> bool:
    """
    Проверка длины строки
    """
    return len(string) < 1000

def isInfoMob(string:str) -> bool:
    """
    Проверка длины строки
    """
    return len(string) < 200

def isInfoSocialValue(social_key:str) -> bool:
    """
    Проверка ссылки для соц сети
    """
    return ("http://" in social_key) or ("https://" in social_key)

def isInfoSocialKey(string:str, questionnaire:Questionnaire) -> bool:
    """
    Проверка ключа для соц сети
    """
    return not(string in questionnaire.info_social.keys()) and len(string) < 50

def isVip(vip:int) -> bool:
    """
    Проверка приоритета (vip)
    если да, запись в бд
    """
    if dbUQuest.check_vip(vip) == 0:
        return True
    else:
        return False
    
def checkAdminPanel(choice: str) -> bool:
    """
    Проверка какая кнопка нажата в админке
    """
    if choice == "create":
        return True
    else:
        return False

def isSub(sub:int) -> bool:
    """
    Проверка оплаты в будущем
    """
    return True

def isNextState(index: int, len_state: int) -> bool:
    """
    Проверка есть ли такое состояние
    """
    return (index +2) < len_state

def allowedText(index_state: int) -> bool:
    """
    Разрешен ли текст в состоянии
    """
    return 0 < index_state < 5

def sendQuest(questionnaire: Questionnaire) -> bool:
    questionnaire.info_social = json.dumps(questionnaire.info_social)
    questionnaire.newQuest()
    questionnaire_tuple = questionnaire.__dict__
    print(questionnaire_tuple)
    questionnaire_tuple = tuple(questionnaire_tuple.values())
    # try:
    dbUQuest.add_new(questionnaire_tuple)
    print(questionnaire_tuple)
    return True
    # except Exception as err:
    #     print(err)
    #     return False
    
    
arrIs = [isImages, isTitle, isPrevie, isInfo, isInfoMob]