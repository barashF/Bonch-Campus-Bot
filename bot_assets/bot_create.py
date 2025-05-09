from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

from middlewares.middleware_exceptions import ValidationErrorMiddleware


def _init_routers(dp: Dispatcher):
    pass

async def main():
    TOKEN = ''
    storage = MemoryStorage()
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bots=bot, storage=storage)

    dp.message.middleware(ValidationErrorMiddleware())
    _init_routers(dp)
    dp.start_polling(bot)


if __name__ == '__main__':
    await main()