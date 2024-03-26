from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import connect_database
from repositories.userRepository import UserRepository
from schemes.authScheme import SignIn, SignUp
from services.authService import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/sign-up")


@router.post("/sign-up")
async def sign_up(user_data: SignUp, session: AsyncSession = Depends(connect_database)):
    user_repository = UserRepository(session)
    auth_service = AuthService(user_repository)
    return await auth_service.sign_up(user_data)

