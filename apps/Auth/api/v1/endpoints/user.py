from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import connect_database
from repositories.userRepository import UserRepository
from schemes.userScheme import UserWithoutPassword
from dependencies.authDependencies import check_authenticate
from services.userService import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/me/", status_code=status.HTTP_200_OK, response_model=UserWithoutPassword)
async def me(
        session: AsyncSession = Depends(connect_database),
        current_user: str = Depends(check_authenticate),
) -> UserWithoutPassword:
    user_repository = UserRepository(session)
    user_service = UserService(user_repository)
    return await user_service.user_info(current_user)
