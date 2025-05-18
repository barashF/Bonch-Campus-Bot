from abc import ABC, abstractmethod


class IEventRepository(ABC):
    @abstractmethod
    async def add(cls, **params):
        pass

    @abstractmethod
    async def get(cls, event_id: int):
        pass
    
    @abstractmethod
    async def get_list(cls, dorm_id: int):
        pass