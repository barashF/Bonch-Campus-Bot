from aiogram.fsm.state import State
from loguru import logger

from dal.interfaces.services.user import IUserService
from dal.interfaces.repositories.user import IUserRepository
from bot_assets.middlewares.exceptions import ValidationError
from utils.states import Registration


class UserService(IUserService):
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def create_user(self, **params):
        self._validate_name(params['name'])
        self._validate_room(params['room'])
        await self.user_repository.add(params)

    def _validate_name(self, name: str):
        if len(name.split()) != 2:
            raise ValidationError(
                message='Необходимо ввести имя и фамилию (Пример: Иван Иванов)',
                state=Registration.name
            )
    
    def _validate_room(self, room: str):
        if not room.isdigit():
            raise ValidationError(
                message='Номер комнаты должен содержать только цифр',
                state=Registration.room
            )