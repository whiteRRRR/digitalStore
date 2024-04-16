from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

class BaseRepository:
    def __init__(self, model, session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def create(self, scheme):
        new_obj = self.model(**scheme.model_dump())

        self.session.add(new_obj)
        await self.session.commit()
        await self.session.refresh(new_obj)
        return new_obj
    
    async def read_all(self):
        stmt = await self.session.execute(
            select(
                self.model
            )
        )
        obj_list = stmt.scalars().all()
        return obj_list
    
    async def read_by_id(self, id: int):
        stmt = await self.session.execute(
            select(
                self.model
            ).where(
                self.model.id == id
            )
        )

        obj_info = stmt.scalar()
        return obj_info
    
    async def update_by_id(self, id: int, scheme):
        try:
            await self.session.execute(
                update(
                    self.model
                ).where(
                    self.model.id == id
                ).values(
                    scheme.model_dump()
                )
            )
            await self.session.commit()
            return "Success full updated"
        except Exception:
            raise Exception("Error")

    async def delete_by_id(self, id: int):
        try:
            await self.session.execute(
                delete(
                    self.model
                ).where(
                    self.model.id == id
                )
            )
            return "Success full deleted item"
        except Exception:
            raise Exception("Error")
        