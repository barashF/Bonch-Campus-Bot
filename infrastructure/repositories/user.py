from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from dal.interfaces.repositories.user import IUserRepository
from infrastructure.database.entities.models import User
from infrastructure.database.db import DataBase
from configuration.config import ADMINS


class UserRepository(IUserRepository):
    
    @classmethod
    @property
    def _sessionmaker(cls):
        return DataBase.sessionmaker

    @classmethod
    async def add(cls, **params):
        async with cls._sessionmaker() as db_context:
            if cls._check_admin(params.get('tg_id')):
                params['data'] = {'privilege':'su'}
            user_entity = User(**params)
            db_context.add(user_entity)
            await db_context.commit()
            await db_context.refresh(user_entity)
            return user_entity
        
    @classmethod
    async def get(cls, tg_id: int) -> User | None:
        async with cls._sessionmaker() as db_context:
            result = await db_context.execute(
                select(User).where(User.tg_id == tg_id)
            )
            user = result.scalar_one_or_none()
            return user
    
    @classmethod
    def _check_admin(cls, tg_id: int):
        if tg_id in ADMINS:
            return True
        return False
    