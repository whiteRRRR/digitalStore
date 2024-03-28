from .baseService import BaseService
from repositories.userRepository import UserRepository
from repositories.authRepository import AuthRepository
from schemes.authScheme import SignUp, SignIn, UserPayload, UserWithToken
from core.security import security


class AuthService(BaseService):

    def __init__(
            self,
            auth_repository: AuthRepository,
            user_repository: UserRepository,
    ):
        self.user_repository = user_repository
        self.auth_repository = auth_repository
        super().__init__(user_repository)

    async def sign_up(self, user_data: SignUp):
        hashed_password = await security.password_security.get_hash_password(user_data.hashed_password)
        user_data.hashed_password = hashed_password
        created_user = await self.add(user_data)
        return created_user

    # TODO: ADD Exceptions
    async def sign_in(self, user_data: SignIn):
        user_info = await self.user_repository.read_user_by_username(user_data.username)
        verify_password = await security.password_security.check_password(user_data.password,
                                                                          user_info.hashed_password)
        if verify_password:
            user_payload = UserPayload(username=user_info.username)
            user_refresh_token = await security.jwt_security.create_refresh_token(user_payload)

            user = UserWithToken(user_id=user_info.id, refresh_token=user_refresh_token)
            create_user_with_token = await self.auth_repository.create(user)
            return create_user_with_token





