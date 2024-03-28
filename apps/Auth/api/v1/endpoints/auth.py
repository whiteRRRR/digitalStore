from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import connect_database
from repositories.userRepository import UserRepository
from repositories.authRepository import AuthRepository
from services.authService import AuthService
from schemes.authScheme import SignIn, SignUp, UserWithoutPassword


router = APIRouter(prefix="/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/sign-up")


@router.post("/sign-up", response_model=UserWithoutPassword)
async def sign_up(user_data: SignUp, session: AsyncSession = Depends(connect_database)) -> UserWithoutPassword:
    user_repository = UserRepository(session)
    auth_repository = AuthRepository(session)
    auth_service = AuthService(auth_repository, user_repository)

    return await auth_service.sign_up(user_data)


@router.post("/sign-in")
async def sign_in(user_data: SignIn, session: AsyncSession = Depends(connect_database)):
    user_repository = UserRepository(session)
    auth_repository = AuthRepository(session)
    auth_service = AuthService(auth_repository, user_repository)

    return await auth_service.sign_in(user_data)
