from aiogram.fsm.state import State
from loguru import logger

from dal.interfaces.services.user import IUserService
from dal.interfaces.repositories.user import IUserRepository
from infrastructure.repositories.user import UserRepository
from bot_assets.middlewares.exceptions import ValidationError
from utils.states import Registration


class UserService(IUserService):
    _user_repository = UserRepository

    @classmethod
    async def validate_name(cls, name: str):
        if len(name.split()) != 2:
            raise ValidationError(
                message='Необходимо ввести имя и фамилию (Пример: Иван Иванов)',
                state=Registration.name
            )
    
    @classmethod
    async def validate_room(cls, room: str):
        if not room.isdigit():
            raise ValidationError(
                message='Номер комнаты должен содержать только цифр',
                state=Registration.room
            )