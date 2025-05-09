from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from loguru import logger
import asyncio

from middlewares.middleware_exceptions import ValidationErrorMiddleware

async def main():
    TOKEN = ''
    storage = MemoryStorage()
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bots=bot, storage=storage)

    logger.add("logs/log_{time}.txt", rotation="12:00")
    
    dp.message.middleware(ValidationErrorMiddleware())
    _init_routers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    await main()