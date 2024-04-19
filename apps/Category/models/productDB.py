from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from core.database import Base

class ProductCategory(Base):
    __tablename__ = "product_category"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    