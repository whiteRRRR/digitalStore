from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from core.config import settings
from typing import Any


class Base(DeclarativeBase):
    pass


async def connection_base() -> Any:
    engine = create_async_engine(settings.database.database_url)
    async_session = async_sessionmaker(engine)
    database = async_session()

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    try:
        yield database
    finally:
        await database.close()
