from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Integer
from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    brands: Mapped[list["Brand"]] = relationship(
        "Brand", back_populates="creator"
    )
    brand_audits: Mapped[list["BrandAudit"]] = relationship(
        "BrandAudit", back_populates="user"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
