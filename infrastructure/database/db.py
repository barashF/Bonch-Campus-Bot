from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from typing import AsyncIterator

from configuration.config import DATABASE_URL


class DataBase:
    _engine = None
    sessionmaker = None

    @classmethod
    async def init(cls, db_url: str = None):
        if db_url is None:
            db_url = os.getenv("DATABASE_URL")
        cls._engine = create_async_engine(db_url, echo=False)
        cls.sessionmaker = async_sessionmaker(cls._engine, expire_on_commit=False)

    @classmethod
    async def close(cls):
        if cls._engine:
            await cls._engine.dispose()
            logger.info("[+] Database engine successfully closed;")