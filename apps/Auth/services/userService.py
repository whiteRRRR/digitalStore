from .baseService import BaseService
from repositories.userRepository import UserRepository


class UserService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        super().__init__(user_repository)

    async def user_info(self, username: str):
        user_data = await self.user_repository.read_user_by_username(username)
        return user_data

