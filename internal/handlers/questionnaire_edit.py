from internal.dispatcher import dp, bot
from internal.сhecks import questionnaire as checksQuest 
from aiogram import types
from aiogram import F
from internal.filters.user_type import IsAdmin
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile, InputMediaPhoto, InputMediaVideo
from internal.app.questionnaire import questionnaire as quest
from aiogram.fsm.context import FSMContext
from internal.states.questionnaire import questionnaire as stateQuest

import json
async def edit_start(webAppMes, state: FSMContext) -> None:
    # print(webAppMes.) #вся информация о сообщении
    # print( "test")
    await state.clear()
    # print("test", webAppMes.web_app_data.data) #конкретно то что мы передали в бота
    questionnaire = webAppMes.web_app_data.data
    # print("web", questionnaire)
    questionnaire_dict = json.loads(questionnaire)
    questionnaire_class = checksQuest.findQuestionnaire(questionnaire_dict)
    await state.update_data(questionnaire = questionnaire_class)
    data = await state.get_data()
    
    string = "HI Hi Hi {}  \n and {}"
    # print(string.format(questionnaire_dict["id"], questionnaire_dict['title']))
    string = questionnaire_dict['title'] + questionnaire_dict['previe'] + questionnaire_dict['info'] + '\n' + questionnaire_dict['info_social'] + '\n' + questionnaire_dict['info_mob']
    # await botsend_message(webAppMes.chat.id, string, parse_mode="HTML")
    image_from_url = URLInputFile(questionnaire_dict['images'][0]['url'])
    if '.webm' in questionnaire_dict['images'][0]['name']:
        image = [InputMediaVideo(media=image_from_url, caption=string, parse_mode="HTML" )]
    else:
        image = [InputMediaPhoto(media=image_from_url, caption=string, parse_mode="HTML" )]

    for i in range(1,len(questionnaire_dict['images'])):
        image_from_url = URLInputFile(questionnaire_dict['images'][i]['url'])
        if '.webm' in questionnaire_dict['images'][i]['name']:
            image.append(InputMediaVideo(media=image_from_url))
        else:
            image.append(InputMediaPhoto(media=image_from_url))
        
    await bot.send_media_group(chat_id=webAppMes.chat.id, media=image)
    await bot.send_message( webAppMes.chat.id, quest.str_edit[0], reply_markup=quest.keyboard_quest_edit) 

async def edit_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    отлпвливаются все хендлеры на первой менюшке изменения анкеты
    там выбираем что менять/закончить изменения/удалить анкету
    """
    await callback.message.edit_text(callback.message.text, reply_markup=None)
    print(callback.data.split("_")[1])
    number = callback.data.split("_")[1]
    if number == "end":
        # data = await state.get_data()
        await bot.send_message( callback.from_user.id, quest.str_end[0][1])
        await state.clear()
    elif number == "delete":
        data = await state.get_data()
        questionnaire = checksQuest.isQuestionnaire(data, callback.from_user.id)
        questionnaire.delQuest()
        if (checksQuest.editQuest(questionnaire)):
            await bot.send_message( callback.from_user.id, quest.str_end[0][2])
        await state.clear()
    else:
        number = int(number)
        await state.update_data(edit = True)
        await state.set_state(stateQuest.arr[number])
        await callback.message.answer(quest.arr_str[number][0], reply_markup=quest.arr_keyboard_edit[number])


dp.message.register(edit_start, IsAdmin(), F.web_app_data)
dp.callback_query.register(edit_callback, IsAdmin(), F.data.startswith("edit") )