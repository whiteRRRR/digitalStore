from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update


class BaseRepository:
    def __init__(self, model, session: AsyncSession):
        self.session = session
        self.model = model

    async def create(self, schema):
        new_obj = self.model(schema.model_dump())

        self.session.add(new_obj)
        await self.session.commit()
        await self.session.refresh(new_obj)
        return new_obj

    async def read_by_id(self, obj_id: int):
        stmt = await self.session.execute(
            select(
                self.model
            ).where(
                self.model.id == obj_id
            )
        )

        obj_info = stmt.scalar()
        return obj_info

    async def update_by_id(self, obj_id: int, schema):
        await self.session.execute(
            update(
                self.model
            ).where(
                self.model.id == obj_id
            ).values(
                schema.model_dump()
            )
        )

        await self.session.commit()

    async def delete_by_id(self, obj_id: int):
        await self.session.execute(
            delete(
                self.model
            ).where(
                self.model.id == obj_id
            )
        )
        await self.session.commit()
