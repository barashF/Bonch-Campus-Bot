from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from loguru import logger
import asyncio

from .middlewares.middleware_exceptions import ValidationErrorMiddleware
from .handlers import start
from utils.test_data import create_dorms
from infrastructure.database.db import DataBase
from configuration.config import DATABASE_URL, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_HOST, POSTGRES_PORT, TOKEN

def _init_routers(dp: Dispatcher):
    dp.include_router(start.router)

async def main():
    storage = MemoryStorage()
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bots=bot, storage=storage)

    logger.add("logs/log_{time}.txt", rotation="12:00")
    
    dp.message.middleware(ValidationErrorMiddleware())
    _init_routers(dp)

    await DataBase.init(DATABASE_URL)
    await dp.start_polling(bot)
    await create_dorms()

