from sqlalchemy import select
from typing import List

from dal.interfaces.repositories.event import IEventRepository
from infrastructure.database.db import DataBase
from infrastructure.database.entities.models import Event


class EventRepository(IEventRepository):
    
    @classmethod
    @property
    def _sessionmaker(cls):
        return DataBase.sessionmaker
    
    @classmethod
    async def add(cls, **params) -> Event:
        async with cls._sessionmaker() as db_context:
            event_entity = Event(**params)
            db_context.add(event_entity)
            await db_context.commit()
            await db_context.refresh(event_entity)
            return event_entity
    
    @classmethod
    async def get(cls, event_id: int) -> Event:
        async with cls._sessionmaker() as db_context:
            result = await db_context.get(Event, event_id)
            return result

    @classmethod
    async def get_list(cls, dorm_id: int) -> List[Event]:
        async with cls._sessionmaker() as db_context:
            result = await db_context.execute(
                select(Event).where(Event.dorm_id == dorm_id)
            )
            return result