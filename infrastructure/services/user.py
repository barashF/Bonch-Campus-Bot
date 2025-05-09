from dal.interfaces.services.user import IUserService
from dal.interfaces.repositories.user import IUserRepository
from dal.models.user import UserCreate
from bot_assets.middlewares.exceptions import ValidationError
from loguru import logger


class UserService(IUserService):
    def __init__(self, user_repository: IUserRepository, current_state: str):
        self.user_repository = user_repository
        self.current_state = current_state

    async def create_user(self, **params):
        try:
            self._validate_name(params['name'])
        except Exception as e:
            # raise e
            logger.error(f"failure to create user, exception {e}")
            return None
                

    async def _validate_name(self, name: str):
        if len(name.split()) != 2:
            raise ValidationError(
                message='Необходимо ввести имя и фамилию (Пример: Иван Иванов)',
                state=self.current_state
            )