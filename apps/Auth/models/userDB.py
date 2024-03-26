from core.database import Base
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, LargeBinary

if TYPE_CHECKING:
    from userTokenDB import UserToken


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(80))
    hashed_password: Mapped[bytes] = mapped_column(LargeBinary)

    user_token: Mapped["UserToken"] = relationship(back_populates="user")
