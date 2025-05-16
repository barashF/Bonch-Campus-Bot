from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from loguru import logger
import asyncio

from .middlewares.middleware_exceptions import ValidationErrorMiddleware
from .handlers import start
from utils.test_data import create_dorms
from infrastructure.database.db import DataBase
from configuration.config import DATABASE_URL, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_HOST, POSTGRES_PORT

def _init_routers(dp: Dispatcher):
    dp.include_router(start.router)

async def create_pool():
    pool = await asyncpg.create_pool(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
    )
    return pool

async def main():
    storage = MemoryStorage()
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bots=bot, storage=storage)

    await create_pool()
    logger.add("logs/log_{time}.txt", rotation="12:00")
    
    dp.message.middleware(ValidationErrorMiddleware())
    _init_routers(dp)

    await DataBase.init(DATABASE_URL)
    await dp.start_polling(bot)
    await create_dorms()

