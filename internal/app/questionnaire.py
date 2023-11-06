from aiogram import types
import os

class questionnaire:
    path = "../images/{}"
    cloudfilename = "/img/{}"
    str_images = ["Загрузите фото\n(Можно загрузить нескольок фото/видео)","", "Я не понимаю ваш текст\nПришлити мне фото"]
    str_title = ["Что будет в первой строчке?", "Попробуйте ввести еще раз"]
    str_previe = ["Что будет во второй строчке?", "Попробуйте ввести еще раз"]
    str_info = ["Что будет в info?", "Попробуйте ввести еще раз"]
    str_info_mob = ["Введите номер телефона?", "Попробуйте ввести еще раз"]
    str_info_social = ["Хотите добавить соц. сети?", "Добавьте ссылку на соц. сети", "К сожалению такая соц. сеть есть\nПопробуйте другую", "Я не понимаю ваш текст\nНажмите на кнопку"]
    str_info_social_edite = ["Вы можете нажать на свою соц. сеть и изменить ссылку \n Или вы можете добавить самостоятельно соц сеть", "Вы можете нажать на кнопку и удалить соц. сеть"]
    str_vip = ["Хотите добавить анкету в топ?", "Это место занято", "Вы выбрали место", "Я не понимаю ваш текст\nНажмите на кнопку"]
    str_sub = ["Хотите оформить подписку?", "Подписка не продлена", "Подписка продлена",  "Я не понимаю ваш текст\nНажмите на кнопку"]
    str_end = [["Анкета записана", "Анкета изменина", "Анкета удалена"], ["Анкета не записана", "Анкета не изменина"]]
    arr_str = [str_images, str_title, str_previe, str_info, str_info_mob,
               str_info_social, str_vip, str_sub, str_end]
    
    str_info_social_value = ["Ссылка добавлена\n", "Отправьте ссылку еще раз"]
    str_info_social_key = ["Введите название соц.сети","К сожалению такая соц. сеть есть или название слишком длинное\nПопробуйте другую\n\nХотите добавить еще одну ссылку на эту соц.сеть?\nДополните название (например Telegram канал)"]

    str_panel = ["Вы можете создать акету\nТак же нажав на изменить вы можете выбрать анкету и изменить ее"]
    url="https://dosugrostov.site/"
    webAppTest = types.WebAppInfo(url = url)
    buttons_quest_panel = [
        [types.InlineKeyboardButton(text="Создать новую анкету", callback_data="quest_create")],
        [types.InlineKeyboardButton(text="Изменить анкету", web_app= webAppTest)]
    ]
    keyboard_quest_panel = types.InlineKeyboardMarkup(inline_keyboard=buttons_quest_panel)

    buttons_quest = [
        [types.InlineKeyboardButton(text="Пропустить этот пункт", callback_data="next")],
        [types.InlineKeyboardButton(text="Отменить все", callback_data="cancel")]
    ]
    keyboard_quest = types.InlineKeyboardMarkup(inline_keyboard=buttons_quest)

    buttons_quest_images = [
        [types.InlineKeyboardButton(text="Отправлены все фотографии", callback_data="images_отмена")],
        [types.InlineKeyboardButton(text="Отменить все", callback_data="cancel")]
    ]
    # [types.InlineKeyboardButton(text="Пропустить этот пункт", callback_data="next")],
    keyboard_quest_images = types.InlineKeyboardMarkup(inline_keyboard=buttons_quest_images)

    buttons_quest_vip = [
        [types.InlineKeyboardButton(text="Первое место", callback_data="vip_1"), 
         types.InlineKeyboardButton(text="Второе место", callback_data="vip_2"), 
         types.InlineKeyboardButton(text="Третье место", callback_data="vip_3")],
        [types.InlineKeyboardButton(text="Пропустить этот пункт", callback_data="next")],
        [types.InlineKeyboardButton(text="Отменить все", callback_data="cancel")]
    ]
    keyboard_quest_vip = types.InlineKeyboardMarkup(inline_keyboard=buttons_quest_vip)

    buttons_quest_sub = [
        [types.InlineKeyboardButton(text="Плюс 15 дней", callback_data="sub_15"), 
         types.InlineKeyboardButton(text="Плюс 30 дней", callback_data="sub_30")],
        [types.InlineKeyboardButton(text="Пропустить этот пункт", callback_data="next")],
        [types.InlineKeyboardButton(text="Отменить все", callback_data="cancel")]
    ]
    keyboard_quest_sub = types.InlineKeyboardMarkup(inline_keyboard=buttons_quest_sub)

    buttons_quest_social = [
        [types.InlineKeyboardButton(text="Telegram", callback_data="social_Telegram"), 
         types.InlineKeyboardButton(text="WhatsApp", callback_data="social_WhatsApp")],
        [types.InlineKeyboardButton(text="Добавить соц. сеть самостоятельно", callback_data="social_add")],
        [types.InlineKeyboardButton(text="Далее", callback_data="next")],
        [types.InlineKeyboardButton(text="Отменить все", callback_data="cancel")]
    ]
    keyboard_quest_social = types.InlineKeyboardMarkup(inline_keyboard=buttons_quest_social)

    arr_keyboard = [keyboard_quest_images, keyboard_quest, 
               keyboard_quest, keyboard_quest, 
               keyboard_quest, keyboard_quest_social, 
               keyboard_quest_vip, keyboard_quest_sub]
    


    button_images = types.InlineKeyboardButton(text="Изменить медиа", callback_data="edit_0")
    button_title =  types.InlineKeyboardButton(text="Изменить название", callback_data="edit_1")
    button_previe = types.InlineKeyboardButton(text="Изменить заголовок", callback_data="edit_2")
    button_info = types.InlineKeyboardButton(text="Изменить основную информацию", callback_data="edit_3")
    button_info_mob = types.InlineKeyboardButton(text="Изменить телефон", callback_data="edit_4")
    button_info_social = types.InlineKeyboardButton(text="Изменить соц.сети", callback_data="edit_5")
    button_vip = types.InlineKeyboardButton(text="Изменить vip", callback_data="edit_6")
    button_sub = types.InlineKeyboardButton(text="Изменить подписку", callback_data="edit_7")
    buttons_quest_edit = [[button_images, button_title], [button_previe, button_info], [button_info_mob,
               button_info_social], [button_vip, button_sub],
               [types.InlineKeyboardButton(text="Закончить изменения", callback_data="edit_end")],
               [types.InlineKeyboardButton(text="Удалить анкету", callback_data="edit_delete")]]
    keyboard_quest_edit = types.InlineKeyboardMarkup(inline_keyboard=buttons_quest_edit)
    buttons_edit = [
        [types.InlineKeyboardButton(text="Изменить", callback_data="edit_True"), types.InlineKeyboardButton(text="Отмена", callback_data="edit_False")]
                    ]
    keyboard_edit = types.InlineKeyboardMarkup(inline_keyboard=buttons_edit)
    str_edit = ['Что вы хотите изменить?']
# --------------------------------------------------
    buttons_edit = [
        [types.InlineKeyboardButton(text="Отменить", callback_data="cancel")]
    ]
    keyboard_edit = types.InlineKeyboardMarkup(inline_keyboard=buttons_edit)

    buttons_edit_images = [
        [types.InlineKeyboardButton(text="Отправлены все фотографии", callback_data="images_отмена")],
        [types.InlineKeyboardButton(text="Отменить", callback_data="cancel")]
    ]
    keyboard_edit_images = types.InlineKeyboardMarkup(inline_keyboard=buttons_edit_images)

    buttons_edit_vip = [
        [types.InlineKeyboardButton(text="Первое место", callback_data="vip_1"), 
         types.InlineKeyboardButton(text="Второе место", callback_data="vip_2"), 
         types.InlineKeyboardButton(text="Третье место", callback_data="vip_3")],
        [types.InlineKeyboardButton(text="Отменить", callback_data="cancel")]
    ]
    keyboard_edit_vip = types.InlineKeyboardMarkup(inline_keyboard=buttons_edit_vip)

    buttons_edit_sub = [
        [types.InlineKeyboardButton(text="Плюс 15 дней", callback_data="sub_15"), 
         types.InlineKeyboardButton(text="Плюс 30 дней", callback_data="sub_30")],
        [types.InlineKeyboardButton(text="Отменить", callback_data="cancel")]
    ]
    keyboard_edit_sub = types.InlineKeyboardMarkup(inline_keyboard=buttons_edit_sub)

    buttons_edit_social = [
        [types.InlineKeyboardButton(text="Удалить", callback_data="social_del")],
        [types.InlineKeyboardButton(text="Изменить/добавить", callback_data="social_edite")],
        [types.InlineKeyboardButton(text="Закончить с соц.сетями", callback_data="social_end")]
    ]
    keyboard_edit_social = types.InlineKeyboardMarkup(inline_keyboard=buttons_edit_social)

    arr_keyboard_edit = [keyboard_edit_images, keyboard_edit, 
               keyboard_edit, keyboard_edit, 
               keyboard_edit, keyboard_edit_social, 
               keyboard_edit_vip, keyboard_edit_sub]
    def keyboardEditeSocial(social: dict, character: bool = True) -> types.InlineKeyboardMarkup:
        """
        создание клавиатуры для удаления/изменения соц.сетей
        character == True, значит изменение 
        """
        buttons = []
        for key, value in social.items():
            print(key, value)
            if character :
                buttons.append([types.InlineKeyboardButton(text=f"{key}", callback_data=f"social_edite_{key}")])
            else:
                buttons.append([types.InlineKeyboardButton(text=f"{key}", callback_data=f"social_del_{key}")])
        if character :
            buttons.append([types.InlineKeyboardButton(text="Добавить соц. сеть самостоятельно", callback_data="social_add")])
        buttons.append([types.InlineKeyboardButton(text="Закончить с соц.сетями", callback_data="social_end")])
        print(buttons)
        return types.InlineKeyboardMarkup(inline_keyboard=buttons)