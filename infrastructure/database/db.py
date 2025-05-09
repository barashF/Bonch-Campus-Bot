from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from typing import AsyncIterator


DATABASE_URL = 'sqlite+aiosqlite:///./bonch.db'
engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session