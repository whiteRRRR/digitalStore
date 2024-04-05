from typing import TYPE_CHECKING
from core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Text, ForeignKey

if TYPE_CHECKING:
    from userDB import User


class UserToken(Base):
    __tablename__ = 'user_token'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'))
    refresh_token: Mapped[str] = mapped_column(Text)

    user: Mapped["User"] = relationship(back_populates="user_token")
