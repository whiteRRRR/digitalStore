from .baseService import BaseService
from fastapi import Response
from core.security import security
from core.exceptions import AuthException
from repositories.userRepository import UserRepository
from repositories.authRepository import AuthRepository
from schemes.authScheme import SignUp, SignIn, TokenData
from schemes.userScheme import UserPayload, UserWithToken


class AuthService(BaseService):

    def __init__(
            self,
            auth_repository: AuthRepository,
            user_repository: UserRepository,
    ):
        self.user_repository = user_repository
        self.auth_repository = auth_repository
        super().__init__(user_repository)

    async def sign_up(self, user_data: SignUp) -> str:
        hashed_password = await security.password_security.get_hash_password(user_data.hashed_password)
        user_data.hashed_password = hashed_password
        await self.add(user_data)
        return "User created successfully"

    async def sign_in(self, user_data: SignIn, response: Response):
        user = await self.user_repository.read_user_by_username(user_data.username)

        if user:
            user_token_exist = await self.auth_repository.read_by_id(user.id)
            verify_password = await security.password_security.check_password(
                user_data.password,
                user.hashed_password
            )
            user_payload = UserPayload(username=user.username)
            user_refresh_token = await security.jwt_security.create_refresh_token(user_payload)
            user_access_token = await security.jwt_security.create_access_token(user_payload)

            if user_token_exist and verify_password:
                await self.auth_repository.update_refresh_token(user.id, user_refresh_token)
                response.set_cookie(key="auth", value=user_refresh_token, httponly=True, secure=True)
                return {"status": "success"}

            if verify_password:
                user = UserWithToken(user_id=user.id, refresh_token=user_refresh_token)
                await self.auth_repository.create(user)
                token_data = TokenData(access_token=user_access_token, token_type="bearer")
                response.set_cookie(key="auth", value=user_refresh_token, httponly=True, secure=True)

                return token_data

        raise AuthException("Incorrect email or password")










