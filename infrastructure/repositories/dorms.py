from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from dal.interfaces.repositories.dorms import IDormRepository
from infrastructure.database.entities.models import Dorm
from infrastructure.database.db import DataBase

class DormRepository(IDormRepository):
    
    @classmethod
    @property
    def _sessionmaker(cls):
        return DataBase.sessionmaker

    @classmethod
    async def add(cls, **params):
        async with cls._sessionmaker() as db_context:
            db_context.add(Dorm(params))
            await db_context.commit()
    
    @classmethod
    async def get(cls, id: int) -> Dorm | None:
        async with cls._sessionmaker() as db_context:
            result = await db_context.get(Dorm, id)
            return result

    @classmethod
    async def get_all_dorms(cls):
        async with cls._sessionmaker() as db_context:
            result = await db_context.execute(
                select(Dorm))
            return result.scalars().all()
