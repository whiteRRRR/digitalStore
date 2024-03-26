from .baseRepository import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from models.userDB import User


class UserRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)
