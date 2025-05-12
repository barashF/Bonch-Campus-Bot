from abc import ABC, abstractmethod


class IUserRepository(ABC):
    @abstractmethod
    async def add(self, **params):
        pass

    @abstractmethod
    async def get(self, tg_id: int):
        pass