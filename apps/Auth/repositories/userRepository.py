from .baseRepository import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.userDB import User


class UserRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def read_user_by_username(self, username: str):
        stmt = await self.session.execute(
            select(
                self.model
            ).where(
                self.model.username == username
            )
        )
        user = stmt.scalar()
        return user
