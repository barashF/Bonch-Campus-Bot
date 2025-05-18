from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router, F

from bot_assets.keyboards.inline import list_events_kb
from infrastructure.repositories.event import EventRepository
from infrastructure.repositories.user import UserRepository
from infrastructure.services.event import EventService


router = Router()


@router.callback_query(F.data == 'events')
async def get_list_events_of_dorm(callback_query: CallbackQuery):
    user = await UserRepository.get(callback_query.from_user.id)
    events = await EventRepository.get_list(user.dorm_id)
    await callback_query.message.edit_reply_markup(reply_markup=None)
    await callback_query.message.answer('Общажные мероприятия:', reply_markup=list_events_kb(events))

@router.callback_query(F.data.startswith('event_'))
async def get_event(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(reply_markup=None)
    event = await EventRepository.get(int(callback_query.data.split('_')[1]))
    kb = InlineKeyboardButton([InlineKeyboardButton(text='Назад', callback_data='events')])
    message = await EventService.get_message_event(event)
    await callback_query.message.answer(message, reply_markup=kb)
