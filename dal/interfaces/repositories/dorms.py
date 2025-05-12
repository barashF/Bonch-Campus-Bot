from abc import ABC, abstractmethod


class IDormRepository(ABC):
    @abstractmethod
    async def add(self, name):
        pass

    @abstractmethod
    async def get(self, id: int):
        pass

    @abstractmethod
    async def get_all_dorms(self):
        pass