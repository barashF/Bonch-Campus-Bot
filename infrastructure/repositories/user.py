from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from dal.interfaces.repositories.user import IUserRepository
from infrastructure.database.entities.models import User
from infrastructure.database.db import DataBase


class UserRepository(IUserRepository):
    
    @classmethod
    @property
    def _sessionmaker(cls):
        return DataBase.sessionmaker

    @classmethod
    async def add(cls, **params):
        async with cls._sessionmaker() as db_context:
            user_entity = User(**params)
            db_context.add(user_entity)
            await db_context.commit()
            await db_context.refresh(user_entity)
        
    @classmethod
    async def get(cls, tg_id: int) -> User | None:
        async with cls._sessionmaker() as db_context:
            result = await db_context.execute(
                select(User).where(User.tg_id == tg_id)
            )
            user = result.scalar_one_or_none()
            return user
    