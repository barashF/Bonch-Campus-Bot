from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from dal.interfaces.repositories.user import IUserRepository
from dal.models.user import UserCreate
from database.entities.models import User


class UserRepository(IUserRepository):
    def __init__(self, db_context: AsyncSession):
        self.db_context = db_context
    
    async def add(self, **params):
        user_entity = User(**params)
        self.db_context.add(user_entity)
        await self.db_context.commit()
        await self.db_context.refresh(user_entity)
        

    async def get(self, tg_id: int) -> User | None:
        result = await self.db_context.execute(
            select(User).where(User.tg_id == tg_id)
        )
        user = result.scalar_one_or_none()
        return user
    