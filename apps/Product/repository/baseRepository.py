from turtle import st
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    def __init__(self, model, session: AsyncSession) -> None:
        self._model = model
        self._session = session
    
    async def create(self, scheme):
        new_product = self._model(**scheme.model_dump())
        
        self._session.add(new_product)
        await self._session.commit()
        await self._session.refresh(new_product)
    
    async def read_all(self):
        stmt = await self._session.execute(
            select(
                self._model
            )
        )

        product_list = stmt.scalars().all()
        return product_list

    async def read_by_id(self, id: int):
        stmt = await self._session.execute(
            select(
                self._model
            ).where(
                self._model.id == id
            )
        )

        product = stmt.scalar()
        return product
    
    async def update_by_id(self, scheme, id: int):
        await self._session.execute(
            update(
                self._model
            ).where(
                self._model.id == id
            ).values(
                scheme.model_dump()
            )
        )
    
    async def delete_by_id(self, id: int):
        await self._session.execute(
            delete(
                self._model
            ).where(
                self._model.id == id
            )
        )
        
        await self._session.commit()


