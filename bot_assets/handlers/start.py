from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

from bot_assets.di import get_user_repository
from bot_assets.keyboards.inline import get_inline_dorms
from infrastructure.repositories.user import UserRepository
from utils.states import Registration


router = Router()


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    user_repository = await get_user_repository()
    tg_id = message.from_user.id

    if await user_repository.get(tg_id):
        await message.answer('Вечер в хату')
    else:
        await message.answer(
            'Вечер в хату, для регистрации необходимо написать Имя и Фамилию'
        )
        await state.set_state(Registration.name)

@router.message(Registration.name, F.text)
async def registration_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text.strip())
    kb_dorms = await get_inline_dorms()
    await message.answer('Заебца, теперь выбери общагу', 
                         reply_markup=kb_dorms.as_markup())
    await state.set_state(Registration.dorm)

