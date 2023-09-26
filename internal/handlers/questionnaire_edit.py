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
    print("test", webAppMes.web_app_data.data) #конкретно то что мы передали в бота
    questionnaire = webAppMes.web_app_data.data
    questionnaire_dict = json.loads(questionnaire)
    questionnaire_class = checksQuest.findQuestionnaire(questionnaire_dict)
    await state.update_data(questionnaire = questionnaire_class)
    data = await state.get_data()
    print(data['questionnaire'])
    string = "HI Hi Hi {}  \n and {}"
    print(string.format(questionnaire_dict["id"], questionnaire_dict['title']))
    print( type(questionnaire_dict))
    print( type(questionnaire_dict['images']))
    print( type(questionnaire_dict['images'][0]))
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
    await callback.message.edit_text(callback.message.text, reply_markup=None)
    print(callback.data.split("_")[1])
    number = int(callback.data.split("_")[1])
    await state.update_data(edit = True)
    await state.set_state(stateQuest.arr[number])
    await callback.message.answer(quest.arr_str[number][0], reply_markup=quest.arr_keyboard_edit[number])


dp.message.register(edit_start, IsAdmin(), F.web_app_data)
dp.callback_query.register(edit_callback, IsAdmin(), F.data.startswith("edit") )