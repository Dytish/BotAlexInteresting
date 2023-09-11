
from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram.fsm.state import State
from internal.сhecks import user as checkUser
from typing import Any, Dict, Optional, Union

from aiogram.types import ContentType
from aiogram.fsm.context import FSMContext
# class HasUsernamesFilter(BaseFilter):
#     async def __call__(self, message: Message, state: State) -> Union[bool, Dict[str, Any]]:
#         # Если entities вообще нет, вернётся None,
#         # в этом случае считаем, что это пустой список
#         entities = message.entities or []

#         # Проверяем любые юзернеймы и извлекаем их из текста
#         # методом extract_from(). Подробнее см. главу
#         # про работу с сообщениями
#         found_usernames = [
#             item.extract_from(message.text) for item in entities
#             if item.type == "mention"
#         ]

#         # Если юзернеймы есть, то "проталкиваем" их в хэндлер
#         # по имени "usernames"
#         if len(found_usernames) > 0:
#             return {"usernames": found_usernames}
#         # Если не нашли ни одного юзернейма, вернём False
#         return False

class IsAdmin(BaseFilter):
    async def __call__(self, message: Message, state: FSMContext) -> bool:
        current_state = await state.get_state()
        # print(current_state)
        
        return checkUser.isAdmin(message.from_user.id) 
    
class IsMedia(BaseFilter):
    async def __call__(self, message: Message) -> bool:

        print(message.content_type)
        return message.content_type == ContentType.PHOTO or message.content_type == ContentType.VIDEO
        # print(current_state)
        
class CheckState(BaseFilter):
    def __init__(self, states: Optional[State] = None) -> None:
        self.states = states
    async def __call__(self, message: Message, state: FSMContext) -> bool:
        current_state = await state.get_state()
        print(current_state in self.states)
        return (current_state in self.states)
    

