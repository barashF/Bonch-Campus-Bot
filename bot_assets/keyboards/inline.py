from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot_assets.di import get_dorm_repository


async def get_inline_dorms():
    dorm_repository = await get_dorm_repository()
    dorms = await dorm_repository.get_all_dorms()

    builder = InlineKeyboardBuilder()
    for dorm in dorms:
        builder.add(
            InlineKeyboardButton(
                text=dorm.name,
                callback_data=f'choice_dorm_{dorm.id}'
            )
        )
    return builder