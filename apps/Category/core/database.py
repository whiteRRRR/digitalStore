from typing import Any
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from core.config import settings


class Base(DeclarativeBase):
    pass


async def connect_database() -> Any:
    engine = create_async_engine(settings.database.database_url)
    async_session = async_sessionmaker(engine)
    database = async_session()

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    try:
        yield database
    finally:
        await database.close()
