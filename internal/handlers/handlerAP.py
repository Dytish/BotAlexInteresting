from internal.dispatcher import bot, dp
from aiogram.filters import Command, CommandStart
from aiogram import types
from aiogram import F
from internal.app.user import user as app_user
from internal.models import user as modelUser
from internal.сhecks import user as checkUser
from aiogram import Router
from internal.filters.user_type import IsMedia

router: Router = Router()
# from internal.database.request_db import request_user_bd

from aiogram.types import ChatMemberUpdated
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, MEMBER, KICKED

@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def user_blocked_bot(event: ChatMemberUpdated):
    status = "KICKED"
    us = modelUser.User(id_telegram=event.from_user.id, 
                         status=status)
    us.type_user = checkUser.isUser(us)
    print("blok", us)

@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
async def user_blocked_bot(event: ChatMemberUpdated):
    status = "MEMBER"
    print("Unblock", event.from_user.id)

# id=236459455

@router.message(Command("s"))
async def process_command(message: types.Message):
    await bot.send_message( 236459455, "str") 

# пригодится на преветсвенные сообщения из сторонних ссылок и то вряд ли
# @dp.message(CommandStart(deep_link='deep_link'))
# async def deep_link(message: types.Message):
#     print(message)
#     await message.answer('Да, знаем мы такое')

async def process_terdsms_command(message: types.Message):
    # print("КОнтакт", message.contact)
    # await bot.send_message( message.chat.id, s)

    user_id = message.from_user.id
    # телефон, емаил
    user = await bot.get_chat(user_id)
    status = "MEMBER"
    us = modelUser.User(user.id, 
                    user.username,
                    user.first_name, user.last_name, 
                    user.bio, 
                    message.from_user.language_code, 
                    message.text, status,
                    message.from_user.is_premium)
    # print(us)
    us.type_user = checkUser.isUser(us)

    await bot.send_message( message.chat.id, app_user.str_start, reply_markup= checkUser.typeСhecking(us.id_telegram) ) 


async def test1(message: types.Message):
    if message.photo:
        # print('foto')
        print(message.photo[-1])
        if message.photo[-1].file_unique_id == "AQADyM8xG_QdsUh-":
            await bot.send_photo(chat_id=message.from_user.id, photo="AgACAgIAAxkBAAIa8GUWybb5qlLoO6oBawQamuhMicnxAALIzzEb9B2xSGXcYp0Rj0U2AQADAgADeQADMAQ")
        # await bot.send_photo(chat_id=message.from_user.id, photo="AQADyM8xG_QdsUh-")
    elif message.video:
        # print('video')
         print(message.video)
   
# @dp.message(F.text)
# async def handle_contact(message: types.Message):
#     print(message.from_user)
#     await bot.send_message(message.chat.id, f"Спасибо! Я получил твой номер телефона: {message}")

dp.message.register(process_terdsms_command, Command("start"))
# dp.message.register(test1, IsMedia())