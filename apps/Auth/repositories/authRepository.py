from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .baseRepository import BaseRepository
from models.userTokenDB import UserToken


class AuthRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(UserToken, session)

    async def update_refresh_token(self, user_id: int, new_refresh_token: str):
        stmt = await self.session.execute(
            select(
                self.model
            ).where(
                self.model.user_id == user_id
            )
        )

        stmt.refresh_token = new_refresh_token
        await self.session.commit()
