from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.baseRepository import BaseRepository
from models.productDB import ProductCategory


class ProductRepository(BaseRepository):
    def __init__(self, ProductCategory, session: AsyncSession) -> None:
        super().__init__(ProductCategory, session)

    async def read_by_name(self, name: str):
        stmt = await self.session.execute(
            select(
                self.model
            ).where(
                self.model.name == name
            )
        )

        category_info = stmt.scalar()
        return category_info