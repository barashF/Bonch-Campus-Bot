from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from infrastructure.repositories.dorms import DormRepository
from infrastructure.database.entities.models import User
from utils.dicts import USER_PRIVILEGE


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

def get_main_kb(privilege):
    kb = [
        [InlineKeyboardButton(text='📅 Календарь мероприятий', callback_data='events'),
         InlineKeyboardButton(text='📜 Правила проживания', callback_data='rules')],
        [InlineKeyboardButton(text='🆘 Поддержка', callback_data='help'),
         InlineKeyboardButton(text='🏆 Кампус Коннект', callback_data='campus_connect')],
        [InlineKeyboardButton(text='👥 Общажное дело', callback_data='dorm_business'),
         InlineKeyboardButton(text='🔍 Поиск жильцов', callback_data='search_tenants')],
        [InlineKeyboardButton(text='⚙️ Настройки', callback_data='settings')]
    ]
    if USER_PRIVILEGE.get(privilege) > 0:
        kb.append([InlineKeyboardButton(text='👑 Управление', callback_data='admin')])
    return InlineKeyboardMarkup(inline_keyboard=kb)

def list_events_kb(events):
    kb = []
    for event in events:
        kb.append([InlineKeyboardButton(text=event.name, callback_data=f'event_{event.id}')])
    kb.append([InlineKeyboardButton(text='Назад', callback_data='main_menu')])
    return InlineKeyboardMarkup(inline_keyboard=kb)

def get_admin_panel():
    kb = [
        [InlineKeyboardButton(text='📅 Создать мероприятие', callback_data='create_event')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

async def get_dorms_kb(user: User, callback: str):

    kb = []
    if USER_PRIVILEGE.get(user.data.get('privilege')) == 3:
        dorms = await DormRepository.get_all_dorms()
        for dorm in dorms:
            kb.append([InlineKeyboardButton(text=dorm.name, callback_data=f'{callback}_dorm_{dorm.id}')])
    else:
        kb.append([InlineKeyboardButton(text=user.dorm.name, callback_data=f'{callback}_dorm_{user.dorm.id}')])
    return InlineKeyboardMarkup(inline_keyboard=kb)

