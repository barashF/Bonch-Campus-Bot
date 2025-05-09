from abc import ABC, abstractmethod

from dal.models.user import UserCreate

class IUserRepository(ABC):
    @abstractmethod
    async def add(self, user: UserCreate):
        pass

    @abstractmethod
    async def get(self, tg_id: int):
        pass