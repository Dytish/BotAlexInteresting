import logging
from aiogram import Bot, Dispatcher

from pkg.config.config import TOKEN
from pkg.config.config import CONFIG_BD
from pkg.database.connection_bd import BD_conn

logging.basicConfig(level=logging.INFO)
bd = BD_conn(CONFIG_BD)
bot = Bot(token=TOKEN)
dp = Dispatcher()