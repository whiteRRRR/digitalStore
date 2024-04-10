from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import connect_database
from repositories.userRepository import UserRepository
from schemes.userScheme import UserWithoutPassword
from dependencies.authDependencies import check_authenticate
from services.userService import UserService
from schemes.userScheme import UserChangePassword, UserResetPassword

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/me/", status_code=status.HTTP_200_OK, response_model=UserWithoutPassword)
async def me(
        session: AsyncSession = Depends(connect_database),
        current_user: str = Depends(check_authenticate),
) -> UserWithoutPassword:
    # Change
    user_repository = UserRepository(session)
    user_service = UserService(user_repository)

    return await user_service.user_info(current_user)


@router.put("/me/change_password/", status_code=status.HTTP_200_OK)
async def change_password(
        passwords: UserChangePassword,
        session: AsyncSession = Depends(connect_database),
        current_user: str = Depends(check_authenticate),
):
    # Change
    user_repository = UserRepository(session)
    user_service = UserService(user_repository)

    return await user_service.change_user_password(current_user, passwords)


@router.delete("/me/delete/", status_code=status.HTTP_202_ACCEPTED)
async def delete_me(
        response: Response,
        session: AsyncSession = Depends(connect_database),
        current_user: str = Depends(check_authenticate),
):
    # Change
    user_repository = UserRepository(session)
    user_service = UserService(user_repository)

    return await user_service.delete_user(response, current_user)


@router.get("/forgot-password")
async def forgot_password(
        email: str,
        session: AsyncSession = Depends(connect_database)
):
    # Change
    user_repository = UserRepository(session)
    user_service = UserService(user_repository)

    return await user_service.forgot_password(email)


@router.put("/resset_password/{secret_key}")
async def reset_password(
        secret_key: str,
        new_password: UserResetPassword,
        session: AsyncSession = Depends(connect_database)
):
    # Change
    user_repository = UserRepository(session)
    user_service = UserService(user_repository)

    return await user_service.resset_password(secret_key, new_password)
