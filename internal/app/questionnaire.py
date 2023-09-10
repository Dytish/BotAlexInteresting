from aiogram import types
import os

class questionnaire:
    str_images = ["Загрузите фото\n(Можно загрузить нескольок фото/видео)","", "Я не понимаю ваш текст\nПришлити мне фото"]
    str_title = ["Что будет в первой строчке?", "Попробуйте ввести еще раз"]
    str_previe = ["Что будет во второй строчке?", "Попробуйте ввести еще раз"]
    str_info = ["Что будет в info?", "Попробуйте ввести еще раз"]
    str_info_mob = ["Есть номер телефона?", "Попробуйте ввести еще раз"]
    str_info_social = ["Хотите добавить соц. сети?", "Добавьте ссылку на соц. сети", "К сожалению такая соц. сеть есть\nПопробуйте другую", "Я не понимаю ваш текст\nНажмите на кнопку"]
    str_vip = ["Хотите добавить анкету в топ?", "Это место занято", "Вы выбрали место", "Я не понимаю ваш текст\nНажмите на кнопку"]
    str_sub = ["Хотите оформить подписку?", "Подписка не продлена", "Подписка продлена",  "Я не понимаю ваш текст\nНажмите на кнопку"]
    str_end = ["Анкета записана", "Анкета не записана"]
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
        [types.InlineKeyboardButton(text="Пропустить этот пункт", callback_data="next")],
        [types.InlineKeyboardButton(text="Отменить все", callback_data="cancel")]
    ]
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
        [types.InlineKeyboardButton(text="Пропустить этот пункт", callback_data="next")],
        [types.InlineKeyboardButton(text="Отменить все", callback_data="cancel")]
    ]
    keyboard_quest_social = types.InlineKeyboardMarkup(inline_keyboard=buttons_quest_social)

    arr_keyboard = [keyboard_quest_images, keyboard_quest, 
               keyboard_quest, keyboard_quest, 
               keyboard_quest, keyboard_quest_social, 
               keyboard_quest_vip, keyboard_quest_sub, 
               str_end]
    

    name = "Test.jpg"
    path = os.path.join(f"pkg/images/{name}")