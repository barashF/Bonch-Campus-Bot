from abc import ABC, abstractmethod


class IUserService(ABC):
    @abstractmethod
    async def create_user(self, **params):
        pass
    