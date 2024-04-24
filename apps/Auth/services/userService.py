import json
from .baseService import BaseService
from repositories.userRepository import UserRepository
from core.security import security
from core.config import SERVER_HOST, settings
from core.exceptions import BadRequestException
from fastapi import Response, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, MessageType
from schemes.userScheme import UserChangePassword, UserEmail, UserResetPassword


class UserService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        super().__init__(user_repository)

    async def user_info(self, username: str):
        user = await self.user_repository.read_user_by_username(username)

        if not user:
            raise BadRequestException("Bad Request")

        return user

    async def delete_user(self, response: Response, username: str):
        user = await self.user_repository.read_user_by_username(username)

        if not user:
            raise BadRequestException("Bad Request")

        await self.user_repository.delete_user_by_username(user.username)
        response.delete_cookie("auth")
        return {"message": "User deleted successfully"}

    async def change_user_password(self, username: str, user_passwords: UserChangePassword):
        user = await self.user_repository.read_user_by_username(username)

        if not user:
            raise BadRequestException("Bad Request")

        if await security.password_security.check_password(user_passwords.old_password, user.hashed_password):
            hashed_password = await security.password_security.get_hash_password(user_passwords.new_password)
            await self.user_repository.update_user_password(user.username, hashed_password)
            return {"message": "Password changed successfully"}

    async def forgot_password(self, email: str):
        user = await self.user_repository.read_user_by_email(email)

        if not user:
            raise BadRequestException("Invalid Email Address")

        fm = FastMail(settings.email.email_conf)
        email_payload = UserEmail(email=email)
        secret_key = await security.jwt_security.create_secret_key(email_payload)
        forgot_url_link = f"{SERVER_HOST}/forgot-password/{secret_key}/"
        email_body = {
            "company_name": settings.email.mail_from,
            "reset_link": forgot_url_link,
        }
        email_body_to_js = json.dumps(email_body)
        message = MessageSchema(
            subject="Password Reset Request",
            recipients=[email],
            template_body=email_body_to_js,
            subtype=MessageType.html
        )

        await fm.send_message(message)
        return {"message": "Email sent successfully"}

    async def resset_password(self, secret_key: str, new_password: UserResetPassword):

        try:
            check_secret_key = await security.jwt_security.decode_jwt(secret_key)
            user_email = check_secret_key["email"]
            user = await self.user_repository.read_user_by_email(user_email)
            hashed_password = await security.password_security.get_hash_password(new_password.new_password)
            await self.user_repository.update_user_password(user.username, hashed_password)
            return {"message": "Password successfully updated"}
        except BadRequestException:
            raise BadRequestException("Invalid email")




















