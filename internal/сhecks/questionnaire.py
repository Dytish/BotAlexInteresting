from internal.models.questionnaire import Questionnaire
from internal.database import questionnaire as dbUQuest
from internal.app.questionnaire import questionnaire as quest
from internal.dispatcher import storage
import os
import json
import pyrebase

def findQuestionnaire(questionnaire: dict) -> Questionnaire:
    """
    Запись словарика в класс модели
    """
    print("social", type(questionnaire["info_social"]), questionnaire["info_social"])
    info_social = json.loads(questionnaire["info_social"])
    print("social", type(info_social))
    questionnaireModel = Questionnaire( user_tg_id=questionnaire["user_tg_id"], images= questionnaire["images"],
                                  title=questionnaire["title"], previe= questionnaire["previe"],
                                  info=questionnaire["info"], info_mob= questionnaire["info_mob"],
                                  info_social=info_social, vip= questionnaire["vip"],
                                  sub=questionnaire["sub"], deleted_at = questionnaire["deleted_at"], active= questionnaire["active"])
    print("ddd", questionnaireModel.__dict__)
    setattr(questionnaireModel, 'created_at', questionnaire["created_at"])
    setattr(questionnaireModel, 'id', questionnaire["id"])
    print("ddd", questionnaireModel.__dict__)
    return questionnaireModel

def isEdit(data: dict) -> bool:
    """
    Проверяет изменение это или добавление новой анкеты
    """
    try:
        edit = data["edit"]
        return True
    except KeyError:
        return False
    
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
    

def isSave( questionnaire:Questionnaire, messages:dict) -> (Questionnaire, str, str):
    """
    Добавление и сохраниение медиа
    """
    if messages.photo:
        # print('foto')
        name = messages.photo[-1].file_id + ".jpg"
    elif messages.video:
        # print('video')
        name = messages.video.file_id + ".WEBM"
        # path = os.path.join(f"pkg/images/{name}")
    questionnaire.images.append(name)
    path = quest.path.format(name)
    print("save", path, name)
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

def prepQuest( questionnaire: Questionnaire ) -> (tuple, list or dict):
    """
    Подготовка анкеты переводим ее в tuple, а фотографий в list
    """
    questionnaire_dict = questionnaire.dict()
    if questionnaire_dict["deleted_at"] == 0:
        questionnaire_dict["deleted_at"] = None
        # del questionnaire_dict["deleted_at"]
    print("aaa", questionnaire.__dict__)
    images = questionnaire_dict["images"]
    # print(questionnaire_dict)
    del questionnaire_dict['images']
    print("aaa", questionnaire.__dict__)
    questionnaire_tuple = tuple(questionnaire_dict.values())
    return questionnaire_tuple, images

def editQuest(questionnaire: Questionnaire) -> bool:
    """
    Изменение анкеты и фотографий
    """
    questionnaire.info_social = json.dumps(questionnaire.info_social)
    questionnaire_tuple, images = prepQuest(questionnaire)
    dbUQuest.edit_quest(questionnaire_tuple)
    questionnaire.info_social = json.loads(questionnaire.info_social)
    print("anketa", questionnaire.__dict__)
    # print(images)
    return True

def sendQuest(questionnaire: Questionnaire) -> bool:
    """
    Сохранение анкеты и фотографий
    """
    questionnaire.info_social = json.dumps(questionnaire.info_social)
    questionnaire.newQuest()
    questionnaire_tuple, images = prepQuest(questionnaire)
    
    # try:
    insertId = dbUQuest.add_new(questionnaire_tuple)
    images_list = []
    for image in images:
        cloudfilename = quest.cloudfilename.format(image) 
        path = quest.path.format(image)
        storage.child(cloudfilename).put(path)
        url = storage.child(cloudfilename).get_url(None)

        images_list.append((image, url, insertId))
    print(questionnaire_tuple)
    dbUQuest.add_new_images(images_list)
    print(images_list)
    return True
    # except Exception as err:
    #     print(err)
    #     return False
    
    
arrIs = [isSave, isTitle, isPrevie, isInfo, isInfoMob]