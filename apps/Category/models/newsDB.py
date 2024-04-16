from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from core.database import Base


class NewsCategoryDB(Base):
    __tablename__ = 'news_category'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
