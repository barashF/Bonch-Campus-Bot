from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from infrastructure.repositories.dorms import DormRepository


async def get_inline_dorms():
    dorms = await DormRepository.get_all_dorms()

    builder = InlineKeyboardBuilder()
    for dorm in dorms:
        builder.add(
            InlineKeyboardButton(
                text=dorm.name,
                callback_data=f'dorm_{dorm.id}'
            )
        )
    return builder

def get_main_kb():
    kb = [
        [InlineKeyboardButton(text='📅 Календарь мероприятий', callback_data='events'),
         InlineKeyboardButton(text='📜 Правила проживания', callback_data='rules')],
        [InlineKeyboardButton(text='🆘 Поддержка', callback_data='help'),
         InlineKeyboardButton(text='🏆 Кампус Коннект', callback_data='campus_connect')],
        [InlineKeyboardButton(text='👥 Общажное дело', callback_data='dorm_business'),
         InlineKeyboardButton(text='🔍 Поиск жильцов', callback_data='search_tenants')],
        [InlineKeyboardButton(text='⚙️ Настройки', callback_data='settings')]
    ]
    return InlineKeyboardMarkup(kb)
