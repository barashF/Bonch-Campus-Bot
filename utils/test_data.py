from infrastructure.database.entities.models import Dorm
from infrastructure.database.db import DataBase
from .dicts import DORMS

from sqlalchemy.ext.asyncio import AsyncSession

async def create_dorms():
    try:
        sessionmaker = DataBase.sessionmaker
        async with sessionmaker() as session:
            for dorm in DORMS.values():
                session.add(Dorm(name=dorm))
            await session.commit()
    except:
        pass