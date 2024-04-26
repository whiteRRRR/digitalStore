from sqlalchemy.ext.asyncio import AsyncSession
from repository.baseRepository import BaseRepository
from models.productDB import Product

class ProductRepository(BaseRepository):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Product, session)

