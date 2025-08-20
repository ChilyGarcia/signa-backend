import enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum
from app.db.base_class import Base


class BrandStatus(str, enum.Enum):
    PENDING = "PENDING"
    REGISTERED = "REGISTERED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"
    CANCELLED = "CANCELLED"


class Brand(Base):
    __tablename__ = "brands"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    owner: Mapped[str] = mapped_column(String(100), nullable=False)
    registration_number: Mapped[str | None] = mapped_column(
        String(100), nullable=True, unique=True
    )
    status: Mapped[BrandStatus] = mapped_column(
        Enum(BrandStatus), nullable=False, default=BrandStatus.PENDING
    )

    def __str__(self):
        return self.name
