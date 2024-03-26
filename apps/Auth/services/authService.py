from .baseService import BaseService
from repositories.userRepository import UserRepository
from repositories.authRepository import AuthorizationRepository
from schemes.authScheme import SignUp
from core.security import security


class AuthService(BaseService):

    def __init__(
            self,
            user_repository: UserRepository,
    ):
        self.user_repository = user_repository

        super().__init__(user_repository)

    async def sign_up(self, user_data: SignUp):
        hashed_password = await security.password_security.get_hash_password(user_data.hashed_password)
        user_data.hashed_password = hashed_password
        created_user = await self.add(user_data)
        return created_user

