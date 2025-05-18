from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

from bot_assets.keyboards.inline import get_admin_panel, get_dorms_kb
from infrastructure.repositories.user import UserRepository
from infrastructure.repositories.event import EventRepository
from infrastructure.services.event import EventService
from utils.states import AddEvent


router = Router()


@router.callback_query(F.data == 'admin')
async def admin_panel(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(reply_markup=None)
    await callback_query.message.answer('Админская панель:', reply_markup=get_admin_panel())

@router.callback_query(F.data == 'create_event')
async def create_event(callback_query: CallbackQuery):
    user = await UserRepository.get(callback_query.from_user.id)
    kb = await get_dorms_kb(user, 'create_event_of')
    await callback_query.message.answer('Выбери общагу:', reply_markup=kb)

@router.callback_query(F.data.startswith('create_event_of_dorm'))
async def add_name_of_event(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.edit_reply_markup(reply_markup=None)
    await callback_query.message.answer('Введи название ивента:')
    await state.update_data(dorm_id=int(callback_query.data.replace('create_event_of_dorm_', '')))
    await state.set_state(AddEvent.name)

@router.message(AddEvent.name, F.text)
async def add_description_of_event(message: Message, state: FSMContext):
    await state.update_data(name=message.text.strip())
    await state.set_state(AddEvent.description)
    await message.answer('Введи описание ивента:')

@router.message(AddEvent.description, F.text)
async def add_datetime_of_event(message: Message, state: FSMContext):
    await state.update_data(description=message.text.strip())
    await state.set_state(AddEvent.datetime)
    await message.answer('Введи дату и время ивента (формат: гггг-mm-dd hh:mm):')

@router.message(AddEvent.datetime, F.text)
async def save_event(message: Message, state: FSMContext):
    datetime = await EventService.validate_datetime(message.text.strip(), state)
    await state.update_data(datetime=datetime)
    data = await state.get_data()
    await EventRepository.add(**data)
    await state.clear()
    await message.answer('Админская панель:', reply_markup=get_admin_panel())
