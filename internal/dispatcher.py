import logging
from aiogram import Bot, Dispatcher

from pkg.config.config import TOKEN
from pkg.config.config import CONFIG_BD
from pkg.config.config import FIRE_BASE_CONFIG
from pkg.database.connection_bd import BD_conn
import pyrebase

firebase=pyrebase.initialize_app(FIRE_BASE_CONFIG)
storage=firebase.storage()
logging.basicConfig(level=logging.INFO)
bd = BD_conn(CONFIG_BD)
bot = Bot(token=TOKEN)
dp = Dispatcher()