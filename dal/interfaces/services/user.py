from abc import ABC, abstractmethod

from models.user import UserCreate


class IUserService(ABC):
    @abstractmethod
    async def create_user(self, user: UserCreate):
        pass
    