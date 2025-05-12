from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from dal.interfaces.repositories.dorms import IDormRepository
from infrastructure.database.entities.models import Dorm
from infrastructure.database.db import DataBase

class DormRepository(IDormRepository):
    def __init__(self):
        self.sessionmaker = DataBase.sessionmaker

    async def add(self, **params):
        async with self.sessionmaker() as db_context:
            db_context.add(Dorm(params))
            await db_context.commit()
    
    async def get(self, id: int) -> Dorm | None:
        async with self.sessionmaker() as db_context:
            result = await db_context.get(Dorm, id)
            return result

    async def get_all_dorms(self):
        async with self.sessionmaker() as db_context:
            result = await db_context.execute(
                select(Dorm))
            return result.scalars().all()
