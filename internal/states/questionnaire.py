from aiogram.fsm.state import State, StatesGroup


class questionnaire(StatesGroup):
    images = State()
    title = State()
    previe = State()
    info = State()
    info_mob = State()
    info_social = State()
    info_social_key = State()
    info_social_value = State()
    vip = State()
    sub = State()
    end = State()
    arr = [images, title, previe, info, info_mob, info_social, vip, sub, end]
    arr_quest = [images, title, previe, info, info_mob, info_social, vip, sub]
    arr_next_end = [images, title, previe, info, info_mob, info_social, info_social_key, info_social_value, vip, sub]

class Social(StatesGroup):
    opt_socila = State()
    social = State()