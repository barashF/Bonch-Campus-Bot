from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

from bot_assets.keyboards.inline import get_inline_dorms
from infrastructure.repositories.user import UserRepository
from infrastructure.services.user import UserService
from utils.states import Registration
from utils.utils import safe_edit_text
from bot_assets.keyboards.inline import get_main_kb


router = Router()


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    tg_id = message.from_user.id
    user = await UserRepository.get(tg_id)
    if user:
        await message.answer(text='Выбери действие:', reply_markup=get_main_kb(user.data.get('privilege')))
    else:
        await message.answer(
            'Вечер в хату, для регистрации необходимо написать Имя и Фамилию'
        )
        await state.set_state(Registration.name)
        await state.update_data(tg_id=int(tg_id))

@router.message(Registration.name, F.text)
async def registration_name(message: Message, state: FSMContext):
    await UserService.validate_name(message.text.strip())
    await state.update_data(name=message.text.strip())

    kb_dorms = await get_inline_dorms()
    await message.answer('Заебца, теперь выбери общагу', 
                         reply_markup=kb_dorms.as_markup())
    await state.set_state(Registration.dorm)

@router.callback_query(F.data.startswith('dorm_'))
async def registration_dorm(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(dorm_id=int(callback_query.data.split('_')[1]))
    await callback_query.message.edit_reply_markup(reply_markup=None)

    await callback_query.message.answer('Охуенно, теперь введи номер комнаты:')
    await state.set_state(Registration.room)

@router.message(Registration.room, F.text)
async def registration_room(message: Message, state: FSMContext):
    await UserService.validate_room(message.text.strip())
    await state.update_data(room=int(message.text.strip()))
    data = await state.get_data()
    await state.clear()

    user = await UserRepository.add(**data)
    await message.answer(text='Выбери действие:', reply_markup=get_main_kb(user.data.get('privilege')))


@router.callback_query(F.data == 'main_menu')
async def get_main_menu(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(reply_markup=None)
    user = await UserRepository.get(callback_query.from_user.id)
    await callback_query.message.answer(text='Выберите действие:',
                                reply_markup=get_main_kb(user.data.get('privilege')))