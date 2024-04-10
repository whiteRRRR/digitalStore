from .baseRepository import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
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

    async def read_user_by_email(self, email: str):
        stmt = await self.session.execute(
            select(
                self.model
            ).where(
                self.model.email == email
            )
        )
        user = stmt.scalar()
        return user

    async def update_user_password(self, username: str, new_password: bytes):
        stmt = await self.session.execute(
            select(
                self.model
            ).where(
                self.model.username == username
            )
        )

        user = stmt.scalar()
        user.hashed_password = new_password
        await self.session.commit()

    async def delete_user_by_username(self, username: str):
        await self.session.execute(
            delete(
                self.model
            ).where(
                self.model.username == username
            )
        )

        await self.session.commit()
