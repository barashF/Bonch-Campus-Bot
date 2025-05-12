from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from dal.interfaces.repositories.user import IUserRepository
from infrastructure.database.entities.models import User
from infrastructure.database.db import DataBase


class UserRepository(IUserRepository):
    def __init__(self):
        self.sessionmaker = DataBase.sessionmaker
    
    async def add(self, **params):
        async with self.sessionmaker() as db_context:
            user_entity = User(**params)
            db_context.add(user_entity)
            await db_context.commit()
            await db_context.refresh(user_entity)
        

    async def get(self, tg_id: int) -> User | None:
        async with self.sessionmaker() as db_context:
            result = await db_context.execute(
                select(User).where(User.tg_id == tg_id)
            )
            user = result.scalar_one_or_none()
            return user
    