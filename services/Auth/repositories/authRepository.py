from sqlalchemy.ext.asyncio import AsyncSession

from baseRepository import BaseRepository
from models.userTokenDB import UserToken


class AuthorizationRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(UserToken, session)

