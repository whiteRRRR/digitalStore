from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from repositories.baseRepository import BaseRepository
from models.newsDB import NewsCategoryDB


class NewsRepository(BaseRepository):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(NewsCategoryDB, session)

    async def read_by_name(self, name: str):
        stmt = await self.session.execute(
            select(
                self.model
            ).where(
                self.model.name == name
            )
        )

        item_info = stmt.scalar()
        return item_info
    

    
