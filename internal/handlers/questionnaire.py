from internal.dispatcher import dp, bot
from internal.models.questionnaire import Questionnaire
from internal.сhecks import questionnaire as checksQuest 
# from internal.database.request_db import request_user_bd
from aiogram.filters import Command, CommandStart
from aiogram import types
from aiogram import F
from internal.app.questionnaire import questionnaire as quest
from internal.states.questionnaire import questionnaire as stateQuest
from aiogram.fsm.context import FSMContext
from aiogram import Router
from internal.filters.user_type import IsAdmin, CheckState, IsMedia



async def admin_panel(message: types.Message, state: FSMContext) -> None:
    """
    Панель администратора
    """
    await state.clear()
    # await state.set_state(stateQuest.arr[0])
    await bot.send_message( message.chat.id, quest.str_panel[0], reply_markup=quest.keyboard_quest_panel) 

async def selection_in_the_admin_panel(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Панель администратора
    """
    await state.clear()
    admin_panel = callback.data.split("_")[1]
    if checksQuest.checkAdminPanel(admin_panel):
        await state.set_state(stateQuest.arr[0])
        await callback.message.answer( quest.arr_str[0][0], reply_markup=quest.arr_keyboard[0]) 
    



async def add_quest(message: types.Message, state: FSMContext) -> None:
    """
    Получаем состояние и его индекс,
    получаем из состояние анкету,
    записывает в необходимый атрибут текст, 
    проверяем разрешен ли текст,
    проходит ли текст проверку, 
    """
    # print(message)
    current_state = await state.get_state()
    index_state = stateQuest.arr.index(current_state)
    # print( current_state)
    data = await state.get_data()
    questionnaire = checksQuest.isQuestionnaire(data, message.from_user.id)
    # print(questionnaire)
    # print(message.html_text)
    if checksQuest.allowedText(index_state):
        # print(checksQuest.arrIs[index_state])
        if checksQuest.arrIs[index_state](message.html_text):
            setattr(questionnaire, questionnaire.arrAttr[index_state], message.html_text)
            # print(questionnaire.__dict__)
            await state.update_data(questionnaire = questionnaire)
            await state.set_state(stateQuest.arr[index_state+1])
            await bot.send_message( message.chat.id, quest.arr_str[index_state+1][0], reply_markup=quest.arr_keyboard[index_state+1])
        else:
            await bot.send_message( message.chat.id, quest.arr_str[index_state][1], reply_markup=quest.arr_keyboard[index_state])
    else:
        await bot.send_message( message.chat.id, quest.arr_str[index_state][-1])

# @dp.callback_query(F.data == "images_отмена", stateQuest.images)

async def add_quest_vip(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Добавить в топ
    """
    current_state = await state.get_state()
    index_state = stateQuest.arr.index(current_state)
    data = await state.get_data()
    print(callback.from_user.id)
    questionnaire = checksQuest.isQuestionnaire(data, callback.from_user.id)
    vip_i = int(callback.data.split("_")[1])
    if checksQuest.isVip(vip_i):
        setattr(questionnaire, questionnaire.arrAttr[index_state], vip_i)
        await state.update_data(questionnaire = questionnaire)
        await state.set_state(stateQuest.arr[index_state+1])
        await callback.message.answer(quest.str_vip[2])
        await callback.message.answer( quest.arr_str[index_state+1][0], reply_markup=quest.arr_keyboard[index_state+1])
    else: 
        await callback.message.answer(quest.str_vip[1])

async def add_quest_sub(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Оформление подписки
    """
    current_state = await state.get_state()
    index_state = stateQuest.arr.index(current_state)
    data = await state.get_data()
    questionnaire = checksQuest.isQuestionnaire(data, callback.from_user.id)
    sub_i = int(callback.data.split("_")[1])
    if checksQuest.isSub(sub_i):
        setattr(questionnaire, questionnaire.arrAttr[index_state], sub_i)
        group_messages = data["media_groups"]
        if group_messages:
            for messages in group_messages:
                try:
                    questionnaire, path = checksQuest.isImages(questionnaire, messages)
                    print(path, type(path))
                    if checksQuest.isAVideo(path):
                        await bot.download(messages.video, destination=path)
                    else:
                        await bot.download(messages.photo[-1], destination=path)
                except FileExistsError: 
                    print("Файл существует")
                else:
                    print('Всё хорошо.')
            await state.set_data({"questionnaire": questionnaire})
        await state.update_data(questionnaire = questionnaire)
        # print(questionnaire.__dict__)
        await callback.message.answer(quest.str_sub[2])

        if checksQuest.sendQuest(questionnaire):
            await state.set_state(stateQuest.arr[index_state+1])
            await callback.message.answer(quest.arr_str[index_state+1][0])
            current_state = await state.get_state()
            if current_state is None:
                return
            await state.clear()
    else: 
        await callback.message.answer(quest.str_sub[1])

        
async def add_quest_social(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Здесь можно выбрать соц сеть
    """
    # current_state = await state.get_state()
    # index_state = stateQuest.arr.index(current_state)
    data = await state.get_data()
    questionnaire = checksQuest.isQuestionnaire(data, callback.from_user.id)
    social_key = callback.data.split("_")[1]
    if social_key == "add":
        await state.set_state(stateQuest.info_social_key)
        await callback.message.answer(quest.str_info_social_key[0])
        return
    if checksQuest.isInfoSocialKey(social_key, questionnaire):
        questionnaire.info_social[social_key] = "" 
        await state.update_data(questionnaire = questionnaire, social_key = social_key)
        # print(questionnaire.__dict__)
        await state.set_state(stateQuest.info_social_value)
        await callback.message.answer(quest.str_info_social[1])
    else:
        await callback.message.answer(quest.str_info_social[2])


async def add_quest_social_value(message: types.Message, state: FSMContext) -> None:
    """
    Добавление ссылки на соц сеть
    """
    data = await state.get_data()
    questionnaire = checksQuest.isQuestionnaire(data, message.from_user.id)
    social_key = data["social_key"]
    if checksQuest.isInfoSocialValue(message.text):
        questionnaire.info_social[social_key] = message.text
        await state.set_state(stateQuest.info_social)
        await bot.send_message( message.chat.id, text= quest.str_info_social_value[0] + quest.str_info_social[0], reply_markup=quest.keyboard_quest_social) 
        await state.set_data({"questionnaire": questionnaire, "media_groups":data["media_groups"]})
    else:
        await bot.send_message( message.chat.id, text= quest.str_info_social_value[1]) 
        

async def add_quest_social_key(message: types.Message, state: FSMContext) -> None:
    """
    Когда добавление соц сети идет самостоятельно
    """
    data = await state.get_data()
    questionnaire = checksQuest.isQuestionnaire(data, message.from_user.id)
    social_key = message.text
    if checksQuest.isInfoSocialKey(social_key, questionnaire):
        questionnaire.info_social[social_key] = "" 
        await state.update_data(questionnaire = questionnaire, social_key = social_key)
        # print(questionnaire.__dict__)
        await state.set_state(stateQuest.info_social_value)
        await bot.send_message(message.chat.id, quest.str_info_social[1])
    else:
        await bot.send_message(message.chat.id, quest.str_info_social_key[1])

async def next_handler_images_end(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Завершение добавления фотографий
    """
    print("end foto", quest.buttons_quest_images[0][0].callback_data)
    
    current_state = await state.get_state()
    index_state = stateQuest.arr.index(current_state)
    data = await state.get_data()
    questionnaire = checksQuest.isQuestionnaire(data, callback.from_user.id)
    data = checksQuest.isMediaGroups(data)
    group_messages = data["media_groups"]
    if group_messages:
        photo_count = len(group_messages)
        await callback.message.answer(f"Спасибо за группу медиа с {photo_count} медиа !")

        await state.set_state(stateQuest.arr[index_state+1])
        await callback.message.answer(quest.arr_str[index_state+1][0], reply_markup=quest.arr_keyboard[index_state+1])
    else:
        await callback.message.answer(quest.arr_str[index_state][0], reply_markup=quest.arr_keyboard[index_state])


async def add_quest_images(message: types.Message, state: FSMContext) -> None:
    """
    Добавление фотографий
    """
    current_state = await state.get_state()
    index_state = stateQuest.arr.index(current_state)
    # print( current_state)
    data = await state.get_data()
    data = checksQuest.isMediaGroups(data)
    data["media_groups"].append(message)
    await state.update_data(media_groups = data["media_groups"])

   





async def next_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Переход к следующему состоянию
    """
    current_state = await state.get_state()
    if current_state is None:
        return
    if "social" in  current_state:
        index_state = stateQuest.arr.index(stateQuest.__name__+":info_social")
    else:
        index_state = stateQuest.arr.index(current_state)
    if checksQuest.isNextState(index_state, len(stateQuest.arr)):
        await state.set_state(stateQuest.arr[index_state+1])
        await callback.message.edit_text(quest.arr_str[index_state][0], reply_markup=None)
        await callback.message.answer(quest.arr_str[index_state+1][0], reply_markup=quest.arr_keyboard[index_state+1])
    else:
        await state.set_state(stateQuest.arr[index_state+1])
        data = await state.get_data()
        questionnaire = checksQuest.isQuestionnaire(data, callback.from_user.id)
        if "media_groups" in data.keys():
            group_messages = data["media_groups"]
            if group_messages:
                photo_count = len(group_messages)
                await callback.message.answer(f"Спасибо за группу медиа с {photo_count} фото, !")

                for messages in group_messages:
                    try:
                        questionnaire, path = checksQuest.isImages(questionnaire, messages)
                        print(path, type(path))
                        if checksQuest.isAVideo(path):
                            await bot.download(messages.video, destination=path)
                        else:
                            await bot.download(messages.photo[-1], destination=path)
                    except FileExistsError: 
                        print("Файл существует")
                    else:
                        print('Всё хорошо.')
                await state.set_data({"questionnaire": questionnaire})
        if checksQuest.sendQuest(questionnaire):
            await callback.message.answer(quest.arr_str[index_state+1][0])
            current_state = await state.get_state()
            if current_state is None:
                return
            await state.clear()
        # дописать запись в бд
    # await callback.message.answer( quest.arr_str[index_state+1][0], reply_markup=quest.keyboard_quest)


async def cancel_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Выход из всех состояний
    """
    current_state = await state.get_state()
    if current_state is None:
        return
    if "social" in  current_state :
        index_state = stateQuest.arr.index(stateQuest.__name__+":info_social")
    else:
        index_state = stateQuest.arr.index(current_state)
    # logging.info("Cancelling state %r", current_state)
    await state.clear()
    await callback.message.edit_text(callback.message.text, reply_markup=None)
    await callback.message.answer(quest.str_end[1])
    # await callback.message.answer( quest.str_end[1]) 
    # await message.answer(
    # "Cancelled.",
    # reply_markup=ReplyKeyboardRemove(),
    # )



dp.message.register(admin_panel, IsAdmin(), F.text == "panel")

dp.callback_query.register(selection_in_the_admin_panel, IsAdmin(), F.data.startswith("quest_create"))

dp.callback_query.register(next_handler, IsAdmin(),  F.data == "next", CheckState(stateQuest.arr_next_end))
dp.callback_query.register(cancel_handler, IsAdmin(), F.data == "cancel", CheckState(stateQuest.arr_next_end) )
# dp.message.register(add_quest, IsAdmin(), stateQuest.images)
dp.message.register(add_quest, IsAdmin(), F.text, CheckState(stateQuest.arr_quest))
dp.callback_query.register(add_quest_vip, IsAdmin(), F.data.startswith("vip"), stateQuest.vip)
dp.callback_query.register(add_quest_sub, IsAdmin(), F.data.startswith("sub"), stateQuest.sub)
dp.callback_query.register(add_quest_social, IsAdmin(), F.data.startswith("social"), stateQuest.info_social)
dp.message.register(add_quest_social_value, IsAdmin(), stateQuest.info_social_value)
dp.message.register(add_quest_social_key, IsAdmin(), stateQuest.info_social_key)
dp.callback_query.register(next_handler_images_end, IsAdmin(), F.data == quest.buttons_quest_images[0][0].callback_data, stateQuest.images)
dp.message.register(add_quest_images, IsAdmin(), IsMedia(), stateQuest.images)


